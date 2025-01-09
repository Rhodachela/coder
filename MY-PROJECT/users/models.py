from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    """
    Custom user model extending AbstractUser.
    Includes unique email, additional fields, and permission compatibility.
    """
    email = models.EmailField(unique=True, help_text="Unique email for each user.")
    first_name = models.CharField(max_length=100, blank=True, help_text="User's first name.")
    last_name = models.CharField(max_length=100, blank=True, help_text="User's last name.")
    is_admin = models.BooleanField(default=False, help_text="Specifies if the user is an admin.")

    # Group and permission fields with unique related names to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.username
