from app.models import User
from app.api.serializers.chat import *
from rest_framework import generics, status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication

class ChatListView(generics.ListAPIView):
    serializer_class = ChatRoomSerializer
    permission_classes = (IsAuthenticated,)  
    authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    def get_queryset(self):
        user=self.request.user
        return ChatRoom.objects.filter(participants__phone=user.phone) 


class MessageHistoryView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    
    def get_queryset(self):
        chatRoomUUID=self.kwargs['chatRoomUUID']
        chatRoom=ChatRoom.objects.get(uuid=chatRoomUUID)
        return chatRoom.messages