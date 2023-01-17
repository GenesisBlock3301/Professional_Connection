from rest_framework import serializers
from accounts.models.users import User
from accounts.models.notification import Notification


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email"]


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class FriendListSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    email = serializers.EmailField(required=True)
