from app.models import User
from app.api.serializers.chat import *
from rest_framework import generics, status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication


class PostView(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
    
    def get_object(self):
        postUUID=self.kwargs['postUUID']
        return Post.objects.get(uuid=postUUID)
    
    def perform_create(self, serializer):
        data=self.request.data
        user=self.request.user
        message = serializer.save(author=user)