import uuid
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from core.utils import get_first_name_from_email


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        """If empty define first name based on email."""
        if not self.first_name:
            self.first_name = get_first_name_from_email(self.email)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


@receiver(pre_save, sender=User)
def set_user_id(sender, instance, **kwargs):
    """Generate and set the user ID before saving the User object."""
    if not instance.id:
        instance.id = uuid.uuid4()


@receiver(post_save, sender=User)
def create_customer_for_user(sender, instance, created, **kwargs):
    """Create a Customer instance for a newly created user."""
    if created:
        Customer.objects.create(user=instance)


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    cpf = models.CharField(max_length=11, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.email


class Permission(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=50)
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return self.user.email


class Address(models.Model):
    customer = models.ForeignKey(
        Customer, related_name='addresses', on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    neighborhood = models.CharField(max_length=100)
    complement = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, \
                 {self.number}, \
                 {self.city}, \
                 {self.state}, \
                 {self.zip_code}"
