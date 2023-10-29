from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount


@admin.register(UserAccount)
class UserAccountAdmin(UserAdmin):
    pass
