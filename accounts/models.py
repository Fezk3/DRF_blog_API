from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Modifying the base user


class CutomUserManager(BaseUserManager):
    # **extra_fields parameter is for the args of the default usermodel
    def create_user(self, email, password, **extra_fields):
        email = self.email = email

        user = self.model(
            email=email,
            **extra_fields
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser most have is_staff on True")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser most have is_superuser on True")

        return self.create_user(email=email, password=password, **extra_fields)


# user model


class User(AbstractUser):
    email = models.EmailField(null=True, max_length=50, unique=True)
    username = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True)

    # config to specify that its needed the Custom manager to create this user
    objects = CutomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username
