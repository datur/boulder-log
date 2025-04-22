from __future__ import annotations
import uuid

from django.db import models

from django.contrib.auth import models as django_auth_models

from boulder_log.data.boulders.models import Boulder
from boulder_log.data.equipment.models import Equipment
from boulder_log.data.locations.models import Location


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

    equipment = models.ManyToManyField(
        "equipment.Equipment",
        related_name="users",
        blank=True,
    )

    climbed_boulders = models.ManyToManyField(
        "boulders.Boulder",
        related_name="climbers",
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.id} - {self.username}"

    @classmethod
    def new(
        cls,
        *,
        username: str,
        password: str,
        email: str,
        first_name: str = "",
        last_name: str = "",
    ) -> User:
        """
        Create a new User instance.
        """
        user = cls.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        return user

    # getters
    def get_created_boulders(self) -> list[Boulder | None]:
        """
        Get the boulders created by this user.
        """
        return list(self.created_boulders.all())

    def get_created_equipment(self) -> list[Equipment | None]:
        """
        Get the equipment created by this user.
        """
        return list(self.created_equipment.all())

    def get_created_locations(self) -> list[Location | None]:
        """
        Get the locations created by this user.
        """
        return list(self.created_locations.all())
