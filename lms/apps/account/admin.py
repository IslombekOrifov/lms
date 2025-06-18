from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

from .models import CustomUser, Role


admin.site.register(Role)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'photo_preview', 'first_name', 
                    'last_name', 'phone', 'is_staff', 'is_active', 'is_verified']
    list_filter = ['is_staff', 'is_superuser', 'is_active',  'is_deleted']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'phone']
    ordering = ['-date_joined']
    
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {
            "fields": (
                "first_name",
                "last_name",
                "email",
                "phone",
                "photo",
                "bio",
                "custom_uuid",
            )
        }),
        (_("Family contacts"), {
            "fields": (
                "father_phone",
                "mother_phone",
                "father_telegram_id",
                "mother_telegram_id",
            ),
            "classes": ("collapse",)  # Сворачиваемый раздел
        }),
        (_("Permissions"), {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            ),
        }),
        (_("Status"), {
            "fields": (
                "is_verified",
                "is_deleted",
                "is_worker",
                "role",
                "school"
            )
        }),
        (_("Important dates"), {
            "fields": (
                "date_joined",
                "last_login",
            )
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'phone',
                'is_staff',
                'is_active'
            ),
        }),
    )
    
    readonly_fields = ['custom_uuid', 'date_joined', 'last_login']
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if not obj: 
            fieldsets = self.add_fieldsets
        return fieldsets
    
    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />', obj.photo.url)
        return "-"
    photo_preview.short_description = 'Photo Preview'