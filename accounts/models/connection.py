from django.db import models
from accounts.models.users import User
from django.core.exceptions import ValidationError


class Connection(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1_connections")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2_connections")

    def save(self, *args, **kwargs):
        if self.user1 == self.user2:
            return ValidationError("User can't connect with self.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user1_id} and {self.user2_id}"

