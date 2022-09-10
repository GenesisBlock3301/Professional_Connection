from django.db import models
from common.models import PostCommon, PostCommentCommon, PostLikeCommon, CommentLikeCommon
from accounts.models.users import User


class Company(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="companies_photo")
    industry = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    about = models.TextField(null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name


class Management(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_managements")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_managements")
    position = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.position


class Experience(models.Model):
    EMPLOYEE_TYPE = [
        ('full_time', "Full-Time"),
        ('part_time', "Part-Time"),
        ("contract", "Contract"),
        ("freelance", "Freelance"),
        ("seasonal", "Seasonal")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_experiences')
    title = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=50, choices=EMPLOYEE_TYPE)
    start = models.DateField()
    end = models.DateField(null=True)
    position = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_experiences")

    @property
    def duration(self):
        return self.end - self.start


class CompanyPost(PostCommon):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_post")

    def __str__(self):
        return f"{self.company_id} post"


class CompanyPostComment(PostCommentCommon):
    company_post = models.ForeignKey(CompanyPost, on_delete=models.CASCADE, related_name="cpost_comment")

    def __str__(self):
        return f"{self.company_post_id}'s comment"


class CompanyPostLike(PostLikeCommon):
    company_post = models.ForeignKey(CompanyPost, on_delete=models.CASCADE, related_name="cpost_like")

    def __str__(self):
        return f"{self.company_post_id}'s like"


class CompanyPostCommentLike(CommentLikeCommon):
    company_comment = models.ForeignKey(CompanyPostComment, on_delete=models.CASCADE, related_name="cp_comment_like")

    def __str__(self):
        return f"{self.company_comment_id} comment like"
