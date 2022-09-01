from rest_framework import serializers
from accounts.models.Featured import Featured
from accounts.models.connection import Connection, Follower
from rest_framework.validators import UniqueTogetherValidator


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Featured
        fields = "__all__"


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = "__all__"

        validators = [
            UniqueTogetherValidator(
                queryset=Connection.objects.all(),
                fields=['user1', 'user2']
            )
        ]


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

