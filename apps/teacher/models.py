from django.apps import apps
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password

from phonenumber_field.modelfields import PhoneNumberField

from ..subject.models import Subject


class TeacherManager(UserManager):

    def _create_user(self, number_phone, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not number_phone:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        user = self.model(number_phone=number_phone, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, number_phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(number_phone, email, password, **extra_fields)

    def create_superuser(self, number_phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(number_phone, email, password, **extra_fields)



class UserTeacher(AbstractUser):

    number_phone = PhoneNumberField(region="KG", unique=True)
    username = models.CharField(blank=True, null=True, max_length=255)
    subject = models.ForeignKey(
        to=Subject,
        related_name="teacherss",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    USERNAME_FIELD: str = 'number_phone'
    REQUIRED_FIELDS = ["username"]

    objects = TeacherManager()

    def __str__(self) -> str:
        return str(self.number_phone)


    class Meta:
        verbose_name = "Tacher"
        verbose_name_plural = "Tachers"