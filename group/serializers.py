from rest_framework import serializers
from .models import GroupPost


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

