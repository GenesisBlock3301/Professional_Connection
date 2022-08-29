from django.db import models
from company.models import Company
from accounts.models.users import User
from .custom_managers import PostManager


class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(Common):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="author_company_posts")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_user_posts")
    text = models.TextField()

    objects = PostManager()

    def __str__(self):
        return f"{self.id}"


class Comment(Common):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    text = models.TextField()

    def __str__(self):
        return f"{self.post_id}'s comment"


class PostLike(Common):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")

    def __str__(self):
        return f"{self.post_id}'s like"


class CommentLike(Common):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment_likes")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="comment_likes")

    def __str__(self):
        return f"{self.comment_id} comment like"


class Tag(Common):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
