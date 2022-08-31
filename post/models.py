from django.db import models
from company.models import Company
from accounts.models.users import User
from .custom_managers import PostManager
from common.models import PostCommon, PostCommentCommon, PostLikeCommon, Common,\
    CommentLikeCommon


class Post(PostCommon):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="author_company_posts")
    objects = PostManager()

    def __str__(self):
        return f"{self.id}"


class Comment(PostCommentCommon):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")

    def __str__(self):
        return f"{self.post_id}'s comment"


class PostLike(PostLikeCommon):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")

    def __str__(self):
        return f"{self.post_id}'s like"


class CommentLike(CommentLikeCommon):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="comment_likes")

    def __str__(self):
        return f"{self.comment_id} comment like"


class Tag(Common):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
