from django.db import models
from accounts.models.users import User


class Group(models.Model):
    group_type = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.FileField(upload_to="group/cover_image", null=True)
    group_photo = models.FileField(upload_to="group/group_photo", null=True)
    industry = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    group_roles = models.TextField(null=True)

    def __str__(self):
        return self.group_name


class GroupMember(models.Model):
    ROLE_TYPE = (
        ("admin", "Admin"),
        ("general", "General")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_group")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group_member")
    role = models.CharField(choices=ROLE_TYPE, max_length=20, null=True)

    def __str__(self):
        return f"{self.group.id}"
