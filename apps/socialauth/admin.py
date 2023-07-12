from django.contrib import admin
from .models import SocialAuthUser
# Register your models here.
@admin.register(SocialAuthUser)
class SocialAuthUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'provider', 'uid', 'extra_data', 'created_at', 'updated_at')

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False