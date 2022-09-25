from rest_framework import serializers
from .models.users import User
from post.serializers import PostSerializer


# class NewsFeedSerializer(serializers.Serializer):
#     posts = PostSerializer()



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
