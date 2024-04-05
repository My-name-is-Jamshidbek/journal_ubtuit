from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    institution = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    academic_degree = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.academic_degree} {self.firstname} {self.lastname}"
