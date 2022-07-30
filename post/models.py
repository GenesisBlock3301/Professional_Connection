from django.db import models
from company.models import Company
from accounts.models.users import User


class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(Common):
    author_company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="author_company_post", null=True)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_users")
    text = models.TextField()

    def __str__(self):
        return f"{self.text[:100]}..."


class Comment(Common):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")
    text = models.TextField()

    def __str__(self):
        return f"{self.text[:100]}..."


class PostLike(Common):
    user = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="user_like")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_like")

    def __str__(self):
        return f"{self.post_id} post like"


class CommentLike(Common):
    user = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="user_comment_like")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="comment_like")

    def __str__(self):
        return f"{self.comment_id} comment like"


class Tag(Common):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
