from django.contrib import admin

from boulder_log.data.boulders import models as boulder_models

admin.site.register(boulder_models.Boulder)
