from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MinValueValidator, MaxValueValidator
from uuid import uuid4


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
    age = models.PositiveIntegerField(
        verbose_name="user age",
        validators=[MinValueValidator(0), MaxValueValidator(120)],
    )

    is_active = models.BooleanField(
        default=True,
    )
    is_contributor = models.BooleanField(
        default=False,
    )
    is_consent = models.BooleanField(
        default=False,
    )
    is_admin = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
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
