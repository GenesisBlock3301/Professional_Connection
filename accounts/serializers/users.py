from rest_framework import serializers
from accounts.models.users import User, Profile, ContactInfo, Notification
from accounts.serializers.others import FeatureSerializer, ConnectionSerializer
from company.serializers import CompanySerializer


class UserSerializer(serializers.ModelSerializer):
    # user_features = FeatureSerializer(many=True)
    # user_connections = ConnectionSerializer(many=True)

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

    # class Meta:
    #     model = Profile
    #     fields = "__all__"
    #
    # def create(self, validated_data):
    #     data = {
    #         "user": validated_data["user"],
    #         "first_name": validated_data["first_name"],
    #         "last_name": validated_data["last_name"],
    #         "image": validated_data.get("image", None),
    #         "website": validated_data.get("website", None)
    #     }
    #     instance = Profile.objects.create(**data)
    #     return instance
    #
    # def update(self, instance, validated_data):
    #     instance.user = validated_data.get("user", instance.user)
    #     instance.first_name = validated_data.get("first_name", instance.first_name)
    #     instance.last_name = validated_data.get("last_name", instance.last_name)
    #     instance.image = validated_data.get("image", instance.image)
    #     instance.website = validated_data.get("website", instance.website)
    #     instance.save()
    #     return instance


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class ContractInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"

