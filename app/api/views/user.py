from app.models import User
from app.api.serializers.user import UserSerializer
from rest_framework import generics, status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication





class UserRegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(serializer.data)
        result={
            "user" : UserSerializer(user, context=self.get_serializer_context()).data
        }
        return JsonResponse(result, status=status.HTTP_201_CREATED)
    
    

class MyProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    
    def get_object(self):
        print(self)
        return User.objects.get(phone=self.request.user.phone)