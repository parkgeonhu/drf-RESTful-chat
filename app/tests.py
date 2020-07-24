# -*- coding: utf-8 -*-

import pytest, json
from app.models import *
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def default_user_data():
    return {
        "phone": "01011111111",
        "password": "!ejrqo401",
        "nickname" : "hello"
    }

@pytest.fixture
def another_user_data():
    return {
        "phone": "01065381788",
        "password": "!ejrqo401",
        "nickname" : "test2"
    }

@pytest.fixture
def default_user_patch_data():
    return {
        "phone": "1",
        "password": "hello",
        "nickname" : "test"
    }


#chat user를 db에 주입
@pytest.fixture
def chat_users(api_client, default_user_data, another_user_data):
    response = api_client.post('/api/auth/sign-up', data=default_user_data)
    response = api_client.post('/api/auth/sign-up', data=another_user_data)

    

@pytest.mark.django_db
def test_auth(api_client, default_user_data, default_user_patch_data):
    #회원가입
    response = api_client.post('/api/auth/sign-up', data=default_user_data)
    assert response.status_code == 201
        
    #로그인
    response = api_client.post('/api/auth/login', data=default_user_data)
    token=response.data['token']
    print(token)
    assert response.status_code == 200

    #내 정보 조회
    api_client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
    response = api_client.get('/api/users/me')
    print(response.data)
    assert response.data['nickname']=='hello'
    
    #내 정보 수정
    api_client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
    response = api_client.patch('/api/users/me', data=default_user_patch_data)
    assert response.status_code == 201
    
    #내 정보 수정한 것의 닉네임이 같은지
    api_client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
    response = api_client.get('/api/users/me')
    assert response.data['nickname']=='test' #닉네임은 바뀌는 필드라는 것인 테스트코드
    assert response.data['phone']!='1' #휴대폰 번호는 안 바뀌는 필드인 것인 테스트코드

@pytest.mark.django_db
def test_chat(api_client, default_user_data, another_user_data, chat_users):
    #default user의 토큰 가져오기
    response = api_client.post('/api/auth/login', data=default_user_data)
    token = response.data['token']

    #another user의 토큰 가져오기
    participant = User.objects.get(phone=another_user_data['phone'])
    participantUUID = participant.uuid
    print(participantUUID)
    api_client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
    
    participants = []
    participants.append(str(participantUUID))
    print(participants)
    chatroom_data={
        "participants" : participants
    }
    print(chatroom_data)
    
    #채팅방의 uuid를 알아내자
    response = api_client.post('/api/chatrooms', data=chatroom_data, format='json')
    assert response.status_code==201
    chatRoomUUID = response.data['uuid']
    
    #채팅방의 uuid를 알아냈으면 메시지를 보낼 준비를 하자
    message_data={
        "chatRoomUUID" : chatRoomUUID,
        "content" : "안녕하세요"
    }
    
    response = api_client.post('/api/messages', data=message_data)
    assert response.status_code==201
    
    #채팅방에 메시지가 잘 갔는지 확인해보자
    response = api_client.get('/api/chatrooms/' + chatRoomUUID)
    assert response.status_code == 200
    assert response.data[0]['content'] == "안녕하세요"