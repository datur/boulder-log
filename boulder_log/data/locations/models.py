from django.db import models


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

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
