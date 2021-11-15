from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ShuleUser

admin.site.register(ShuleUser, UserAdmin)


