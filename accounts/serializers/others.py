from rest_framework import serializers
from accounts.models.Featured import Featured
from accounts.models.connection import Connection, Follower


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Featured
        fields = "__all__"


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = "__all__"


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = "__all__"

