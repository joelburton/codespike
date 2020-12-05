from django.contrib import admin
from users.admin import UserAdmin

from .models import StaffMember


@admin.register(StaffMember)
class StaffMemberAdmin(UserAdmin):
    """Admin for a staff member."""
