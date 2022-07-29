from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from ..subject.models import Subject


class TeacherManager(models.Manager):

    def get_all_classes(self):
        return self.classes.all()


class Teacher(models.Model):

    number_phone = PhoneNumberField(region="KG")
    subject = models.ForeignKey(
        to=Subject,
        related_name="teachers",
        on_delete=models.SET_NULL,
        null=True
    )
    
    objects = TeacherManager()

