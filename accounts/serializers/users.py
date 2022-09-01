from rest_framework import serializers
from accounts.models.users import User, Profile, ContactInfo, Notification


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    """
    Create serializer for Profile database
    """
    class Meta:
        model = Profile
        fields = "__all__"

    def create(self, validated_data):
        data = {
            "user": validated_data["user"],
            "first_name": validated_data["first_name"],
            "last_name": validated_data["last_name"],
            "image": validated_data.get("image", None),
            "website": validated_data.get("website", None)
        }
        instance = Profile.objects.create(**data)
        return instance

    def update(self, instance, validated_data):
        instance.user = validated_data.get("user", instance.user)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.image = validated_data.get("image", instance.image)
        instance.website = validated_data.get("website", instance.website)
        instance.save()
        return instance


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class ContractInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"

