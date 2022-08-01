from django.db import models
from accounts.models.users import User


class Featured(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_features")
    documents = models.FileField(upload_to="featured_photos")

    def __str__(self):
        return f"{self.user.first_name}+ {self.user.last_name} featured"

