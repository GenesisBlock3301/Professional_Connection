from accounts.models.users import User, Profile
from django.core.exceptions import ValidationError


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def validate_user_associate_with_user(sender, instance, **kwargs):
    if instance.user:
        instance.save()
    else:
        raise ValidationError("Profile's user not created")

