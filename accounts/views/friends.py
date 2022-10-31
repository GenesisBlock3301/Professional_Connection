import logging
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status

from accounts.serializers.users import FriendListSerializer
from common.helper import HelperAdapter
from accounts.helper import FriendHelper
from common.responses import FRIEND_ACTION_RESPONSE, GET_DATA_FROM_SERIALIZER
from accounts.models.users import Profile, Notification
from accounts.models.connection import Connection, Follower


User = get_user_model()
logger = logging.getLogger(__name__)


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
                name = profile.first_name + " " + profile.last_name if profile.first_name and profile.last_name \
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


class FriendList(APIView):
    def get(self, request, pk=None):
        users = HelperAdapter(common_helper=FriendHelper(request=request))
        if pk:
            data = users.get_item(pk)
            serializer = FriendListSerializer(data)
            return Response(GET_DATA_FROM_SERIALIZER(serializer))
        else:
            return users.pagination(users.my_items(request.user.id), FriendListSerializer)


class BlockedFriendList(APIView):
    permissions = [permissions.IsAuthenticated, ]

    @staticmethod
    def __blocked_remove_or_add(from_user, to_user, is_blocked):
        try:
            if is_blocked:
                from_user.block_friends.add(to_user)
                to_user.block_friends.add(from_user)
            else:
                from_user.block_friends.remove(to_user)
                to_user.block_friends.remove(from_user)
        except Exception as e:
            logger.critical(str(e), exc_info=True)
            return Response(FRIEND_ACTION_RESPONSE["block_failed"], status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            users = HelperAdapter(common_helper=FriendHelper(request=request))
            users.pagination(users.my_items(request.user.id))
        except Exception as e:
            logger.critical(str(e), exc_info=True)
            return Response(FRIEND_ACTION_RESPONSE["request_critical_failed"], status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        from_user = request.user
        friend_id = request.query_params.get('friend_id')
        is_blocked = request.query_params.get('is_blocked')
        to_user = User.objects.get(id=int(friend_id))
        self.__blocked_remove_or_add(from_user, to_user, is_blocked)
        if is_blocked:
            return Response(FRIEND_ACTION_RESPONSE["blocked"], status=status.HTTP_200_OK)
        return Response(FRIEND_ACTION_RESPONSE["block_failed"], status=status.HTTP_200_OK)
