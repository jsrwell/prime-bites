from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.text import slugify


class PrimeUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and save a user with the given email and password."""
        if not email:
            raise ValueError("The Email field must be set.")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """ Create and save a superuser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = PrimeUserManager()

    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        if not self.first_name:
            self.first_name = self.get_first_name_from_email()

        super().save(*args, **kwargs)

    def get_first_name_from_email(self):
        """Get the first name from the first part of the e-mail."""
        email_parts = self.email.split("@")
        name = email_parts[0]
        name = slugify(name)
        return name.split("-")[0]

    def __str__(self):
        return self.email
