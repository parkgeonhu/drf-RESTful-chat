from app.models import User
from app.api.serializers.user import *
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
    
    
    # def patch(self, request, *args, **kwargs):
    #     try:
    #         query=request.data['location_approximate']
    #     except KeyError:
    #         return self.partial_update(request, *args, **kwargs)
    #     info=get_location_info(query)
    #     location=InfoEntity(info)
    #     request.data['dong_cd']=location.get_dong_cd()
    #     request.data['dong_cd2']=location.get_dong_cd2()
        
    #     manager=self.get_manager(request.data['dong_cd'], request.data['dong_cd2'])
    #     car=self.get_object()
        
    #     #차의 위치가 바뀌어 이슈의 상태도 바뀌어야 할 때
    #     for issue in car.issues.filter(status='ASSIGN'):
    #         issue.performer=manager
    #         issue.save()
            
    #     request.data['location_x']=location.get_x()
    #     request.data['location_y']=location.get_y()
    #     return self.partial_update(request, *args, **kwargs)
    

class MyProfileView(generics.RetrieveAPIView, generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    
    def get_object(self):
        print(self)
        return User.objects.get(phone=self.request.user.phone)
    
    def patch(self, request, *args, **kwargs):
        user=self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            try:
                request.data['password']
                user.set_password(request.data['password'])
            except KeyError:
                pass
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse("wrong parameters", status=status.HTTP_400_BAD_REQUEST)