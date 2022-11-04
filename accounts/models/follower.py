from django.db import models
from accounts.models.users import User
from django.core.exceptions import ValidationError


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followings")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.user == self.follower:
            return ValidationError("User can't follow self.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user_id} - {self.follower_id}"
