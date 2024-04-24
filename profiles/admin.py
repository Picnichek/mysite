from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerProfile, PerformerProfile, CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('User type', {'fields': ('user_type',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomerProfile)
admin.site.register(PerformerProfile)
