from django.conf import settings
from django.db import models

from general_app.validators import image_max_size

User = settings.AUTH_USER_MODEL

# Create your models here

ACTIVE = "Active"
INACTIVE = "Inactive"
STATUS_CHOICES = [(ACTIVE, "Active"), (INACTIVE, "Inactive")]


class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=25, null=True, blank=True)
    mobile = models.CharField(max_length=14, null=True, blank=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=ACTIVE)
    county = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    postal_code = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(
        upload_to="community/images", validators=[image_max_size], null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        name = self.name if self.name else "name is not set yet"
        return name


ROLE_CHOICES = [
    ("Operations", "Operations"),
    ("Sales", "Sales"),
    ("HR", "HR"),
    ("Branch Manager", "Branch Manager"),
]


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=25, null=True, blank=True)
    mobile = models.CharField(max_length=14, null=True, blank=True)
    role = models.CharField(max_length=16, choices=ROLE_CHOICES)
    county = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    postal_code = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(
        upload_to="community/images", validators=[image_max_size], null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
