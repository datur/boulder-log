from django.db import models


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
    photo = models.ImageField(upload_to="equipment", verbose_name="Photo", blank=True)
    is_private = models.BooleanField(default=False, verbose_name="Is Private")

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
