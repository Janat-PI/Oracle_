from django.db import models

from ..classes.models import Classes


class School(models.Model):

    title = models.CharField(
        "название",
        max_length=255,
        unique=True
    )

    classes = models.ForeignKey(
        to=Classes, 
        related_name="school", 
        on_delete=models.PROTECT
        )

    def __str__(self) -> str:
        return f"pk: {self.pk} | {self.title}"

    class Meta:
        verbose_name = "Schools"
        verbose_name_plural = "School"