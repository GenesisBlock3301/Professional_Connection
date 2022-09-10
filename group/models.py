from django.db import models
from accounts.models.users import User
from common.models import Common
from common.models import PostCommon, PostLikeCommon, CommentLikeCommon, PostCommentCommon, CommonUserField


class Group(Common):
    group_type = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.FileField(upload_to="group/cover_image", null=True)
    group_photo = models.FileField(upload_to="group/group_photo", null=True)
    industry = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    group_roles = models.TextField(null=True)
    is_public = models.BooleanField(default=True, help_text="group will visible to others user.")
    allow_connection = models.BooleanField(default=True, help_text="allow connection to general user")

    def __str__(self):
        return self.group_name


class GroupMember(CommonUserField):
    ROLE_TYPE = (
        ("admin", "Admin"),
        ("general", "General")
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group_members")
    role = models.CharField(choices=ROLE_TYPE, max_length=20, null=True)

    def __str__(self):
        return f"{self.group_id}"


class GroupPost(PostCommon):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group_member")

    def __str__(self):
        return f"{self.group_id} post"


class GroupPostComment(PostCommentCommon):
    group_post = models.ForeignKey(GroupPost, on_delete=models.CASCADE, related_name="post_comment")

    def __str__(self):
        return f"{self.group_post_id}'s comment"


class GroupPostLike(PostLikeCommon):
    group_post = models.ForeignKey(GroupPost, on_delete=models.CASCADE, related_name="gp_like")

    def __str__(self):
        return f"{self.group_post_id}'s like"


class GroupPostCommentLike(CommentLikeCommon):
    group_comment = models.ForeignKey(GroupPostComment, on_delete=models.CASCADE, related_name="gp_comment_like")

    def __str__(self):
        return f"{self.group_comment_id} comment like"
