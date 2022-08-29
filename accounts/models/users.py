from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models import Count
from datetime import date
from datetime import date, timedelta


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str):
        """
        Create general user method
        """
        if not email:
            raise ValueError('Email must be specified!')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(self._db)
        return user

    def create_superuser(self, email: str, password: str):
        """
        Create superuser method
        """
        if not email:
            raise ValueError('Email must be specified!')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(self._db)
        return user

    def get_queryset(self):
        return super().get_queryset().annotate(num_of_connection=Count("user1_connections")).all()


class User(AbstractBaseUser):
    """Custom user model"""
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True,
    )
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profiles")
    first_name = models.CharField(_("First Name"), max_length=255, null=True, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="user_photo", null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_notifications")
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} {self.message[:50]}.."


class ContactInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_contracts")
    profile_link = models.CharField(max_length=1000, null=True)
    website = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=16, null=True)
    email = models.CharField(max_length=100, null=True)
    birthdate = models.DateField(null=True, max_length=8)

    def calculate_age(self):
        return (date.today() - self.birthdate) // timedelta(days=365.2425)
