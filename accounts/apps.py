from django.apps import AppConfig
from django.db.models.signals import post_save, pre_save
from signals import create_profile, validate_user_associate_with_user
from accounts.models.users import User, Profile


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        post_save.connect(create_profile, sender=User)
        pre_save(validate_user_associate_with_user, sender=Profile)
