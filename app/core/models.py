"""
Database models.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager of users."""
    def create_user(self, email, password=None, **extra_field):
        """Create, save and returna  new user."""
        user = self.model(email=email, **extra_field)
        user.set_password(password)
        user.save(using=self._db)
        return user



# AbstUsr.. Authentication features.... and PermMixin Permissions Features
class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'