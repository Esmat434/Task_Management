from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser,PasswordResetToken
)

@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username",'email')}),
        ("Personal info", {"fields": ("first_name", "last_name", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2"),
            },
        ),
    )

@admin.register(PasswordResetToken)
class PasswordResetTokenAdmin(admin.ModelAdmin):
    list_display = ['user','token','created_at']