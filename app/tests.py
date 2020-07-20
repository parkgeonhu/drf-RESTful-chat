import pytest
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

@pytest.mark.django_db 
def test_auth(api_client, default_user_data):
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