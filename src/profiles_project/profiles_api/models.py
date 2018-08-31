from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """helps django work with our custom user model"""

    def Create_User(self, email, name, password=None):
        """Create a new user profile object"""

        if not email:
            raise ValueError('Users must have an Email Address.')

        email = self.normalize_email(email)
        user = self.model(email=email , name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,name,email,password):
        """Creates and saves a new superuser with given details."""

        user = self.Create_User(email, name, password)

        user.is_superuser= True
        user.is_staff=True

        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a "user profile" inside our system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    # UserName Field and the required field is a default attribute should be provided for profile creation and required in django user models

    def get_full_name(self):
        """Used to get a users full name."""

        return self.name

    def get_short_name(self):
        """Used to get a users short name."""

        return self.name

    def __str__(self):
        """django uses this when it needs to convert the object to a string"""

        return self.email
