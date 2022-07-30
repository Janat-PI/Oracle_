from django.db import models

from ..teacher.models import UserTeacher
from ..student.models import Student


class Classes(models.Model):
    
    title = models.CharField(
        "название класса",
        max_length=255,
        unique=True
    )

    teacher = models.OneToOneField(
        to=UserTeacher,
        related_name="classes",
        on_delete=models.SET_NULL,
        null=True
    )

    students = models.ForeignKey(
        to=Student,
        related_name="classes",
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.teacher} {self.title}"

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"