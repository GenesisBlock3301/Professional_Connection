from accounts.models.users import Profile
from django.db.models import Q
from accounts.models.connection import Connection, Follower
from rest_framework.response import Response
from accounts.responses import ELEMENT_NOT_EXIST
from company.models import Company


class ProfileHelper:
    def __init__(self, request):
        self.request = request

    def get_profile_information(self):
        profile = Profile.objects.select_related("user").filter(user=self.request.user).first()
        if not profile:
            return Response(ELEMENT_NOT_EXIST)
        number_of_connections = Connection.objects.select_related("user1", "user2").filter(user1=self.request.user)\
            .count()
        number_of_followers = Follower.objects.select_related("user", "follower").filter(user=self.request.user).count()
        params = (
                Q(follower=self.request.user) &
                Q(follower__isnull=False))
        following = Follower.objects.select_related("user", "follower").filter(params).count()
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
