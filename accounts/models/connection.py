from django.db import models
from accounts.models.users import User
from django.core.exceptions import ValidationError


class Connection(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user1_connections")
    user2 = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user2_connections")

    def __str__(self):
        return f"{self.user1.first_name} and {self.user2.last_name}"
