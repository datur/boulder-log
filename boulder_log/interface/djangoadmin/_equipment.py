from django.contrib import admin

from boulder_log.data.equipment import models as equipment_models

admin.site.register(equipment_models.Equipment)
