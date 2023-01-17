from rest_framework import serializers
from accounts.models.follower import Follower
from rest_framework.validators import UniqueTogetherValidator


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = "__all__"

        validators = [
            UniqueTogetherValidator(
                queryset=Follower.objects.all(),
                fields=['user', 'follower']
            )
        ]
