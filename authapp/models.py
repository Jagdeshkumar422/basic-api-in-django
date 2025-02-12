from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to="profile_images/", null=True, blank=True)
    role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('user', 'User')], default='user')

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",  # Custom related name
        blank=True
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",  # Custom related name
        blank=True
    )
