from django.db import models
from accounts.models.users import User


class Connection(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user1.first_name} and {self.user2.last_name}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.user1_id == self.user2_id:
            raise ValueError("Both users can't be same")

