from __future__ import annotations
from django.db import models
from PIL import Image


class Location(models.Model):
    """
    A location where a boulder can be found.
    """

    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, verbose_name="Latitude"
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, verbose_name="Longitude"
    )
    floor_plan_map = models.ImageField(
        upload_to="locations", verbose_name="Floor Plan Map", blank=True
    )
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Date Added")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Date Modified")
    is_private = models.BooleanField(default=False, verbose_name="Is Private")

    created_by = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="created_locations",
    )

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"

    @classmethod
    def new(
        cls,
        *,
        name: str,
        description: str,
        latitude: float,
        longitude: float,
        created_by_id: int,
        is_private: bool = False,
        floor_plan_map: Image = None,
    ) -> Location:
        """
        Create a new Location instance.
        """
        return cls.objects.create(
            name=name,
            description=description,
            latitude=latitude,
            longitude=longitude,
            is_private=is_private,
            floor_plan_map=floor_plan_map,
            created_by_id=created_by_id,
        )

    @property
    def is_public(self) -> bool:
        """
        Check if the location is public.
        """
        return not self.is_private
