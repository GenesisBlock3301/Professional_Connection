from django.db import models
from accounts.models.users import User


class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CommonUserField(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PostCommon(CommonUserField):
    text = models.TextField()

    class Meta:
        abstract = True


class PostCommentCommon(CommonUserField):
    text = models.TextField()

    class Meta:
        abstract = True


class PostLikeCommon(CommonUserField):
    class Meta:
        abstract = True


class CommentLikeCommon(CommonUserField):
    class Meta:
        abstract = True
