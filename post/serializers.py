from rest_framework import serializers
from .models import Post


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):

    num_of_likes = serializers.IntegerField()
    num_of_comments = serializers.IntegerField()

    class Meta:
        model = Post
        ordering = ['-id']
        fields = "__all__"

