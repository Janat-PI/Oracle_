from django.db import models


class StudentManager(models.Manager):

    def get_class(self):
        return self.classes.all()
        


class Student(models.Model):

    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other")
    )

    first_name = models.CharField(
        "first_name",
        max_length=255,
        blank=True,
        null=True
    )

    full_name = models.CharField(
        "full_name",
        max_length=255,
        blank=True,
        null=True
    )

    email = models.EmailField(
        "email",
        unique=True,
        default="test@gmail.com"
    )

    date_of_birth = models.DateField(
        "date_of_birth",
        blank=True,
        null=True
    )

    address = models.TextField(
        "address",
        blank=True,
        null=True
        )

    sex = models.CharField(
        "gender",
        max_length=6,
        choices=GENDER,
        blank=True, 
        null=True
    )

    image = models.ImageField(
        "students/",
        blank=True, 
        null=True
    )

    objects: StudentManager = StudentManager()

    def __str__(self) -> str:
        # if self.objects.get_class().exists():
        #     return f'{self.first_name} {self.objects.get_class()}'
        return f' {self.pk} {self.first_name}'