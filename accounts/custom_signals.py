from accounts.models.users import Profile, User
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# @receiver(pre_save, sender=Profile)
# def validate_user_associate_with_user(sender, instance, **kwargs):
#     if instance.user:
#         instance.save()
#     else:
#         raise ValidationError("Profile's user not created")

