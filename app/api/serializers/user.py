from app.models import User
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    
    phone=serializers.CharField()
    nickname=serializers.CharField()
    password=serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        print(validated_data)
        return User.objects.create_user(**validated_data)
    
    class Meta:
        model = User
        fields = ['phone', 'nickname', 'password']