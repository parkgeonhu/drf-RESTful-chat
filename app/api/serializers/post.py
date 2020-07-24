 from app.models import *
from rest_framework import serializers

from .user import *

class PostSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)
    
    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    class Meta:
        model = Post
        fields = ('__all__')