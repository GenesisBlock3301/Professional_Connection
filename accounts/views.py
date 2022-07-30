from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics, status
from .serializers import UserSerializer
from .schemas.users_schemas import signup_request_schema_body, signup_response_schema_body
User = get_user_model()


class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(request_body=signup_request_schema_body, responses=signup_response_schema_body)
    def post(self, request):
        data = self.request.data
        email = data['email']
        password = data['password']
        password2 = data['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'})
            else:
                if len(password) < 6:
                    return Response({'error': "Password must be at least 6 character"})
                else:
                    user = User.objects.create_user(email=email, password=password)
                    user.save()
                    return Response({"code": status.HTTP_200_OK, "status": "User created successfully"})
        else:
            return Response({'error': "Password not match"})


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
