from rest_framework import serializers
from .models import GroupPost, Group


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = "__all__"


class AllGroupSerializer(serializers.ModelSerializer):
    num_of_members = serializers.IntegerField(required=True)

    class Meta:
        model = Group
        fields = ("group_type", "group_name", "num_of_members")


class CreateGroupPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupPost
        fields = "__all__"


class GroupPostSerializer(serializers.ModelSerializer):

    num_of_likes = serializers.IntegerField()
    num_of_comments = serializers.IntegerField()

    class Meta:
        model = GroupPost
        ordering = ['-id']
        fields = "__all__"

