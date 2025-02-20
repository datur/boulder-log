from django.contrib import admin

from boulder_log.data.locations import models as location_models

admin.site.register(location_models.Location)
