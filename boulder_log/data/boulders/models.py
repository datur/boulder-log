from __future__ import annotations
from django.db import models
from PIL import Image


class Boulder(models.Model):
    """
    A boulder that a user can log.
    """

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    grade = models.CharField(max_length=255, verbose_name="Grade")
    style = models.CharField(max_length=255, verbose_name="Style")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Date Added")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Date Modified")
    photo = models.ImageField(
        upload_to="boulders",
        verbose_name="Photo",
        null=True,
    )
    segmented_image = models.ImageField(
        upload_to="boulders",
        verbose_name="Segmented Image",
        null=True,
    )
    is_private = models.BooleanField(default=False, verbose_name="Is Private")

    location = models.OneToOneField(
        "locations.Location",
        on_delete=models.CASCADE,
        related_name="boulders",
    )

    created_by = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="created_boulders",
    )

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"

    @classmethod
    def new(
        cls,
        *,
        name: str,
        description: str,
        grade: str,
        style: str,
        location_id: int,
        created_by_id: int,
        is_private: bool = False,
        photo: Image = None,
        segmented_image: Image = None,
    ) -> Boulder:
        """
        Create a new Boulder instance.
        """
        return cls.objects.create(
            name=name,
            description=description,
            grade=grade,
            style=style,
            is_private=is_private,
            location_id=location_id,
            photo=photo,
            segmented_image=segmented_image,
            created_by_id=created_by_id,
        )

    # Properties
    @property
    def is_public(self) -> bool:
        """
        Check if the boulder is public.
        """
        return not self.is_private
