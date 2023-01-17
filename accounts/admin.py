from django.contrib import admin
from accounts.models.users import User, Profile
from accounts.models.connection import Connection
from accounts.models.Featured import Featured


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id", "email"
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id", "first_name", "last_name"
    )


# @admin.register(Connection)
# class UserAdmin(admin.ModelAdmin):
#     list_display = (
#         "user1", "user2"
#     )
#
#
# @admin.register(Featured)
# class UserAdmin(admin.ModelAdmin):
#     pass
