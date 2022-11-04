from datetime import timedelta

from django.db import models
from accounts.models.users import User


class ContactInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_contracts")
    profile_link = models.CharField(max_length=1000, null=True)
    website = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=16, null=True)
    email = models.CharField(max_length=100, null=True)
    birthdate = models.DateField(null=True, max_length=8)

    def calculate_age(self):
        return (date.today() - self.birthdate) // timedelta(days=365.2425)
