import logging
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.decorators import login_required
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
from accounts.models.connection import Connection, Follower

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


@login_required
def send_friend_request(request, user_id):
    try:
        from_user = request.user
        to_user = User.objects.filter(id=user_id).first()
        friend_request, created = Connection.objects.get_or_create(user1=from_user, user2=to_user)
        if created:
            follower = Follower.objects.create(user=to_user, follower=from_user)
            follower.save()
            return Response({"message": "Request send successfully."}, status=status.HTTP_200_OK)

        if friend_request.accepted_or_rejected == "accepted":
            return Response({"message": "you are already friend."}, status=status.HTTP_200_OK)
        return Response({"message": "Request not send"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.critical(str(e), exc_info=True)
        return Response({"message": "send request not perform or you are already friend"},
                        status=status.HTTP_400_BAD_REQUEST)


@login_required
def accept_friend_request(request, connection_id):
    try:
        params = Q(
            Q(accepted_or_rejected=None) &
            Q(id=connection_id)
        )
        friend_request = Connection.objects.filter(params).first()
        if friend_request.user2 == request.user:
            follower = Follower.objects.create(user=friend_request.user1, follower=request.user)
            follower.save()
            friend_request.accepted_or_rejected = "accepted"
            friend_request.save()
            return Response({"message": "Request accept successfully."}, status=status.HTTP_200_OK)
    except Exception as e:
        logger.critical(str(e), exc_info=True)
        return Response({"message": "accept request not perform"}, status=status.HTTP_400_BAD_REQUEST)


@login_required
def delete_friend_request_0r_already_friend(request, connection_id):
    try:

        friend = Connection.objects.filter(id=connection_id).first()
        follower = Follower.objects.filter(Q(user=friend.user1, follower=friend.user2) | Q(user=friend.user2,
                                                                                           follower=friend.user1))
        follower.delete()
        friend.delete()
        return Response({"message": "friend deleted successfully."}, status=status.HTTP_200_OK)
    except Exception as e:
        logger.critical(str(e), exc_info=True)
        return Response({"message": "delete request not perform"}, status=status.HTTP_400_BAD_REQUEST)
