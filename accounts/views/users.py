import logging
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.serializers.users import ProfileSerializer, UserSerializer, CreateProfileSerializer

from common.responses import POST_ERROR_RESPONSE, POST_SUCCESS_RESPONSE, POST_EXCEPTION_ERROR_RESPONSE, \
    GET_DATA_FROM_SERIALIZER, FRIEND_ACTION_RESPONSE
from accounts.models.users import Profile, Notification
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


class SendFriendRequest(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, user_id):
        try:
            from_user = request.user
            profile = Profile.objects.get(user=from_user)
            if not profile:
                return Response(FRIEND_ACTION_RESPONSE["has_profile"], status=status.HTTP_200_OK)
            to_user = User.objects.get(id=user_id)
            is_friend = from_user.friends.filter(id=from_user.id).exists()
            if is_friend:
                return Response(FRIEND_ACTION_RESPONSE["already_friend"], status=status.HTTP_200_OK)
            friend_request, created = Connection.objects.get_or_create(user1=from_user, user2=to_user)
            if created:
                Follower.objects.create(user=to_user, follower=from_user)
                name = profile.first_name + " " + profile.last_name if profile.first_name and profile.last_name\
                    else None
                message = f"{name if name else from_user.id} send you friend request"
                Notification.objects.create(user=to_user, message=message)
                return Response(FRIEND_ACTION_RESPONSE["sent_request"], status=status.HTTP_200_OK)
            return Response(FRIEND_ACTION_RESPONSE["sent_request_failed"], status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.critical(str(e), exc_info=True)
            return Response(FRIEND_ACTION_RESPONSE["request_critical_failed"], status=status.HTTP_400_BAD_REQUEST)


class AcceptFriendRequest(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, connection_id):
        try:
            friend_request = Connection.objects.filter(id=connection_id).first()
            profile = Profile.objects.filter(user=friend_request.user2).first()
            if not profile:
                return Response(FRIEND_ACTION_RESPONSE["has_profile"], status=status.HTTP_200_OK)
            if friend_request.user2 == request.user:
                friend_request.user2.friends.add(friend_request.user1)
                friend_request.user1.friends.add(friend_request.user2)
                Follower.objects.create(user=friend_request.user1, follower=request.user)
                name = profile.first_name + " " + profile.last_name if profile.first_name and profile.last_name else None
                message = f"{name if name else friend_request.user2_id} accept your friend request."
                Notification.objects.create(user=friend_request.user1, message=message)
                friend_request.delete()
                return Response(FRIEND_ACTION_RESPONSE["accept_request"], status=status.HTTP_200_OK)
            return Response(FRIEND_ACTION_RESPONSE["unauthorized_for_accept"],
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.critical(str(e), exc_info=True)
            return Response(FRIEND_ACTION_RESPONSE["request_critical_failed"], status=status.HTTP_400_BAD_REQUEST)


class DeleteFriendRequestOrAlreadyFriend(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, friend_id):
        try:
            from_user = User.objects.get(id=request.user.id)
            to_user = User.objects.get(id=friend_id)
            from_user.friends.remove(to_user)
            to_user.friends.remove(from_user)
            Follower.objects.filter(
                Q(user__id=friend_id, follower__id=request.user.id) |
                Q(user__id=request.user.id,
                  follower=friend_id)).delete()
            return Response(FRIEND_ACTION_RESPONSE["delete_successfully"], status=status.HTTP_200_OK)
        except Exception as e:
            logger.critical(str(e), exc_info=True)
            return Response(FRIEND_ACTION_RESPONSE["request_critical_failed"], status=status.HTTP_400_BAD_REQUEST)


class BlockFriendList(APIView):
    pass