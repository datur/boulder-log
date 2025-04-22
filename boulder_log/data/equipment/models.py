from __future__ import annotations
from django.db import models

from PIL import Image


class Equipment(models.Model):
    """
    A piece of equipment that a user can own.
    """

    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Name")
    brand = models.CharField(max_length=255, verbose_name="Brand")
    equipment_type = models.CharField(max_length=255, verbose_name="Type")
    description = models.TextField(verbose_name="Description")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Date Added")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Date Modified")
    photo = models.ImageField(upload_to="equipment", verbose_name="Photo", null=True)
    is_private = models.BooleanField(default=False, verbose_name="Is Private")

    created_by = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="created_equipment",
    )

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"

    @classmethod
    def new(
        cls,
        *,
        name: str,
        brand: str,
        equipment_type: str,
        description: str,
        created_by_id: int,
        is_private: bool = False,
        photo: Image = None,
    ) -> Equipment:
        """
        Create a new Equipment instance.
        """
        return cls.objects.create(
            name=name,
            brand=brand,
            equipment_type=equipment_type,
            description=description,
            is_private=is_private,
            photo=photo,
            created_by_id=created_by_id,
        )

    @property
    def is_public(self) -> bool:
        """
        Check if the equipment is public.
        """
        return not self.is_private
