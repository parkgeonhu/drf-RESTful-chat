# from rest_framework.response import Response
# from rest_framework.views import APIView


# class LoginView(APIView):
# 	def post(self, request):
# 		phone=request.data.get('phone')
# 		password=request.data.get('password')
# 		user=authenticate(phone=phone,password=password)
		
# 		if user:
# 			token, created=Token.objects.get_or_create(user=user)
# 			data={'token' : token.key}
# 			return Response(data, status=status.HTTP_201_CREATED)		
# 		raise exceptions.AuthenticationFailed('인증 정보 x')


# class LogoutView(APIView):
# 	authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
# 	def get(self, request, format=None):
# 		request.user.auth_token.delete()
# 		return Response(status=status.HTTP_200_OK)
    
#[TO-DO] 추후 phoneAuth 토큰활용해야함