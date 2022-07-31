from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserTeacher


class UserTacherAdmin(UserAdmin):
    list_display = ["number_phone", "get_full_name", "is_active", "is_staff"]


admin.site.register(UserTeacher, UserTacherAdmin)
