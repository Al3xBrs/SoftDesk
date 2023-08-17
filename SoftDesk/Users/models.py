from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.forms import forms
from uuid import uuid4
from datetime import date
from django.contrib.auth.models import PermissionsMixin


class AnyUserManager(BaseUserManager):
    def create_user(self, email, username, password, date_of_birth):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username, date_of_birth):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            username=username,
            date_of_birth=date_of_birth,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)


class AnyUser(AbstractBaseUser, PermissionsMixin):
    objects = AnyUserManager()

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(
        verbose_name="email address",
        max_length=100,
        unique=True,
    )
    username = models.CharField(
        verbose_name="username",
        unique=True,
        max_length=50,
    )

    #   Age verify. Has to be more than 15.
    date_of_birth = models.DateField(
        "user dob",
    )

    def age_verification(self):
        dob = self.date_of_birth
        today = date.today
        if (dob.year + 15, dob.month, dob.day) > (
            today.year,
            today.month,
            today.day,
        ):
            raise forms.ValidationError(
                "Vous devez être agé d'au moins 15 ans pour vous inscrire."
            )
        return dob

    is_active = models.BooleanField(
        default=True,
    )
    is_contributor = models.BooleanField(
        default=False,
    )

    can_be_contacted = models.BooleanField(
        default=False,
    )

    can_data_be_shared = models.BooleanField(
        default=False,
    )

    is_admin = models.BooleanField(
        default=False,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_superuser = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "email",
        "date_of_birth",
    ]


class Contributor(models.Model):
    username = models.CharField(
        verbose_name="username",
        unique=True,
        max_length=50,
    )
    email = models.EmailField(
        verbose_name="email address",
        max_length=100,
        unique=True,
    )
