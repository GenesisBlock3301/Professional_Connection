from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Email must be specified!')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(self._db)
        return user

    def create_superuser(self, email, password):
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


class User(AbstractBaseUser):
    """The user model, it is a user profile as well"""
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True,

    )
    first_name = models.CharField(_("First Name"), max_length=255, null=True, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="user_photo", null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def has_perm(self):
        return self.is_superuser

    def has_module_perms(self):
        return self.is_superuser

    def __str__(self):
        return self.email
