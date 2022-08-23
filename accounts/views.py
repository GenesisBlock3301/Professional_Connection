from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
User = get_user_model()


class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = self.request.data
        email = data['email']
        password = data['password1']
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


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.META.get("HTTP_REFRESH_TOKEN")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"status": "Successfully logout"},
                            status=status.HTTP_205_RESET_CONTENT)
        except Exception  as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = [
            permissions.IsAuthenticated
        ]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

