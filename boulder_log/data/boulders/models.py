from django.db import models


class Boulder(models.Model):
    """
    A boulder that a user can log.
    """

    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    grade = models.CharField(max_length=255, verbose_name="Grade")
    style = models.CharField(max_length=255, verbose_name="Style")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Date Added")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Date Modified")
    photo = models.ImageField(upload_to="boulders", verbose_name="Photo", blank=True)
    segmented_image = models.ImageField(
        upload_to="boulders", verbose_name="Segmented Image", blank=True
    )
    is_private = models.BooleanField(default=False, verbose_name="Is Private")

    # TODO: Add location field once the Location model is created.

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
