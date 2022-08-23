from django.core.management.base import BaseCommand, CommandError
from accounts.models.users import User
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            if not user.is_staff or not user.is_superuser:
                user.set_password(user.password)
                user.save()

