# from django.db import models
# from django.contrib.auth.models import AbstractUser

# # Create your models here.
# class CustomUser(AbstractUser):
#     class Role(models.TextChoices):
#         STUDENT = "STUDENT", "Student"
#         INSTRUCTOR = "INSTRUCTOR", "Instructor"
#         ADMIN = "ADMIN", "Administrator"

#     role = models.CharField(max_length=10,
#             choices= Role.choices, 
#             default = Role.STUDENT)

#     course = models.CharField(max_length=100, blank=True)

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        CONSUMER = "CONSUMER", "Consumer"
        BAKERY = "BAKERY", "Bakery Owner"

    role = models.CharField(
        max_length=15,
        choices=Role.choices,
        default=Role.CONSUMER
    )
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    bakery_name = models.CharField(max_length=150, blank=True)