from app.models import *
from rest_framework import serializers

from .user import *

class MessageSerializer(serializers.ModelSerializer):
    
    senderUUID = serializers.SlugRelatedField(source='sender', slug_field='uuid', read_only=True)
    
    senderNickname = serializers.SlugRelatedField(source='sender', slug_field='nickname', read_only=True)
    
    def create(self, validated_data):
        return Message.objects.create(**validated_data)
    
    class Meta:
        model = Message
        fields = ['senderUUID','senderNickname','content']

class ChatRoomSerializer(serializers.ModelSerializer):
    
    #messages = MessageSerializer(many=True, read_only=True)
    participants = ProfileSerializer(many=True, read_only=True)
    
    class Meta:
        model = ChatRoom
        exclude = ('messages',)