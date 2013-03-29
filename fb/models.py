# Define a custom User class to work with django-social-auth
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, first_name=None, last_name=None, gender=None, **extra_fields):
        """
        Creates and saves a User with the given fields.
        """
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
            email=MyUserManager.normalize_email(email),
            first_name=first_name or '',
            last_name=last_name or '',
            gender=gender or 'unknown'
        )


        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, first_name=None, last_name=None, gender=None):
        """
        Creates and saves a superuser with the given fields.
        """
        user = self.create_user(
            username,
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            gender=gender
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'gender']

    def get_full_name(self):
        # The user is identified by their first and last name
        return self.first_name + self.last_name

    def get_short_name(self):
        # The user is identified by their first and last name
        return self.first_name + self.last_name

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin