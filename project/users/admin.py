from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User

# Don't actually show this in the admin, since it's confusing for others ---
# they should directly use "Staff member" or "Student" sections in admin.
#
# Under the hood, though, those are just proxy models for User, and everyone would
# be found here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Admin for all users on the site.

    Generally, this won't be very useful --- it's easier to add/edit users and staff by
    doing so directly in the admin. This is useful for non-staff, non-student users (if
    any), and to make those subclasses DRY.
    """
