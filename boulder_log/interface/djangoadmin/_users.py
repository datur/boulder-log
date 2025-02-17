from django.contrib import admin

from boulder_log.data.users import models as user_models

admin.site.register(user_models.User)
