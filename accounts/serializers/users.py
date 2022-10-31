from rest_framework import serializers
from accounts.models.users import User, Profile, ContactInfo, Notification
from company.serializers import CompanySerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email"]


class CreateProfileSerializer(serializers.ModelSerializer):
    """
    Create serializer for Profile database
    """

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileSerializer(serializers.Serializer):
    """
    Create serializer for Profile database
    """
    user = UserSerializer()
    company = CompanySerializer()
    first_name = serializers.CharField(max_length=255, required=False)
    last_name = serializers.CharField(max_length=255, required=False)
    image = serializers.ImageField(required=False)
    website = serializers.CharField(max_length=255)
    number_of_friends = serializers.IntegerField()
    number_of_followers = serializers.IntegerField()
    following = serializers.IntegerField()


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class ContractInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"


class FriendListSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    email = serializers.EmailField(required=True)
