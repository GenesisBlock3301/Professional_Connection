from django.db.models import Q, Count
from rest_framework.response import Response
from accounts.models.users import Profile
from accounts.models.connection import Connection, Follower
from common.pagination import CustomPagination
from common.responses import ELEMENT_NOT_EXIST
from common.helper import CommonIterableItem
from company.models import Company
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileHelper:
    def __init__(self, request):
        self.request = request
        self.profile = Profile.objects.select_related("user")
        self.follower = Follower.objects.select_related("user", "follower")
        self.connection = Connection.objects.select_related("user1", "user2")

    def get_profile_information(self):
        profile = self.profile.filter(user=self.request.user).first()
        if not profile:
            return Response(ELEMENT_NOT_EXIST)
        number_of_connections = self.connection.filter(user1=self.request.user).count()
        number_of_followers = self.follower.filter(user=self.request.user).count()
        params = (
                Q(follower=self.request.user) &
                Q(follower__isnull=False))
        following = self.follower.filter(params).count()
        company = Company.objects.select_related("manager").filter(manager=self.request.user).first()

        data = {
            "user": profile.user,
            "company": company,
            'first_name': profile.first_name,
            "last_name": profile.last_name,
            "image": profile.image if profile.image else None,
            "website": profile.website if profile.website else None,
            "number_of_friends": number_of_connections,
            "number_of_followers": number_of_followers,
            "following": following
        }
        return data

    def refectoring_post_data(self):
        data = {
            "user": self.request.user.id,
            "first_name": self.request.data.get("first_name", ""),
            "last_name": self.request.data.get("last_name", ""),
            "image": self.request.data.get("image", None),
            "website": self.request.data.get("website", "")
        }
        return data


class FriendHelper(CommonIterableItem):
    def __init__(self, request):
        self.request = request
        self.user = User.objects.prefetch_related("friends")

    def get_item(self, friend_id):
        pass

    def my_items(self, user_id):
        return self.user.get(id=user_id).friends.values("id", "email").order_by("-id")

    def all_items(self):
        pass

    def pagination(self, data, serializer_class):
        paginator = CustomPagination()
        result_page = paginator.get_queryset(data=data, request=self.request)
        serializer = serializer_class(result_page, many=True)
        return paginator.get_response(serializer.data)
