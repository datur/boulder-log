import uuid

from django.db import models

from django.contrib.auth import models as django_auth_models


class User(django_auth_models.AbstractUser):
    """
    A person who can log in to the application.
    """

    id = models.AutoField(primary_key=True, verbose_name="ID")
    uuid = models.UUIDField(
        default=uuid.uuid4,
        verbose_name="UUID",
        editable=False,
    )

    def __str__(self) -> str:
        return f"{self.id} - {self.username}"
