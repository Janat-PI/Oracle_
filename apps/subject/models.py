from django.db import models


class Subject(models.Model):

    title = models.CharField(
        "название предмета",
        max_length=255,
        unique=True
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
