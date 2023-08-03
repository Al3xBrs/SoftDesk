from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.forms import forms
from uuid import uuid4
from datetime import date


class AnyUser(AbstractBaseUser):
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
        dob = self.cleaned_data["date_of_birth"]
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

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "email",
        "age",
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
