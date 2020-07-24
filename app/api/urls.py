from django.urls import re_path, path

# from .views.auth import LoginView
from .views.userviews import MyProfileView, UserRegisterView
from .views.chatviews import *
from .views.postviews import *

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    
	# 자신의 정보 GET
	path('users/me', MyProfileView.as_view()),
	
	# 로그인
	path('auth/login', obtain_jwt_token),
    path('auth/sign-up', UserRegisterView.as_view(),  ),
    
    #토큰 갱신
    path('token/refresh', refresh_jwt_token),
    
    path('token/verify', verify_jwt_token),
    
    #Post
    path('posts', PostView.as_view()),
    path('posts/<uuid:postUUID>', PostView.as_view()),
    
    #Chat, ChatRoom
    path('chatrooms', ChatRoomCreateView.as_view()),
    path('chatrooms/<uuid:chatRoomUUID>',ChatRoomHistoryView.as_view()),
    
    #Message
    path('messages', MessageView.as_view()),
]