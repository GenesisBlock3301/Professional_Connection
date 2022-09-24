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
    WHO_CAN_SEE_POST = (
        ("everyone", "everyone"),
        ("public", "public"),
        ("only_me", "only-me")
    )

    WHO_CAN_COMMENT = (
        ("everyone", "everyone"),
        ("public", "public"),
        ("only_connection", "only connection")
    )

    who_can_view = models.CharField(max_length=20, choices=WHO_CAN_SEE_POST, default="public")
    who_can_comment = models.CharField(max_length=25, choices=WHO_CAN_COMMENT, default="public")
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
