import logging
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.serializers.users import ProfileSerializer, UserSerializer, CreateProfileSerializer

from common.responses import POST_ERROR_RESPONSE, POST_SUCCESS_RESPONSE, POST_EXCEPTION_ERROR_RESPONSE, \
    GET_DATA_FROM_SERIALIZER
from accounts.models.users import Profile
from accounts.helper import ProfileHelper

User = get_user_model()
logger = logging.getLogger(__name__)


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
                    return Response(POST_SUCCESS_RESPONSE)
        else:
            return Response(POST_ERROR_RESPONSE)


class ProfileApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            instance = Profile.objects.filter(user=request.user).first()
        except Profile.DoesNotExist:
            instance = None

        try:
            profile = ProfileHelper(request)
            data = profile.refectoring_post_data()
            serializer = CreateProfileSerializer(instance=instance, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(POST_SUCCESS_RESPONSE)
            return Response(POST_ERROR_RESPONSE)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            return Response(POST_EXCEPTION_ERROR_RESPONSE)

    def get(self, request):
        profile = ProfileHelper(request)
        data = profile.get_profile_information()
        serializer = ProfileSerializer(data)
        return Response(GET_DATA_FROM_SERIALIZER(serializer))


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.META.get("HTTP_REFRESH_TOKEN")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"status": "Successfully logout"},
                            status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

