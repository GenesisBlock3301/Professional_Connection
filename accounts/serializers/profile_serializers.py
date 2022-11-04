from rest_framework import serializers
from accounts.models.profile import Profile
from accounts.serializers.user_serializers import UserSerializer
from company.serializers import CompanySerializer


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
