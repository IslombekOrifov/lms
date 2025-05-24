from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator


class RoleName(models.TextChoices):
    ADMIN = 'admin', _('Administrator')
    DEKAN = 'dekan', _('Dean')
    RECTOR = 'rector', _('Rector')
    DEPARTMENT_USER = 'department_user', _('Department User')
    TUTOR = 'tutor', _('Tutor')
    STYLIST = 'stylist', _('Stylist')
    ACCOUNTANT = 'accountant', _('Accountant')
    TEACHER = 'teacher', _('Teacher')
    STUDENT = 'student', _('Student')


class Role(models.Model):
    name = models.CharField(
        max_length=50,
        choices=RoleName.choices,
        unique=True,
        verbose_name=_('Role Name')
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Description')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created At')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated At')
    )

    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')
        ordering = ['name']

    def __str__(self):
        return self.get_name_display()

    @classmethod
    def create_default_roles(cls):
        """Создает стандартные роли при необходимости"""
        for role_id, role_name in RoleName.choices:
            cls.objects.get_or_create(name=role_id)
            

class CustomUser(AbstractUser):
    
    phone = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(_("first name"), max_length=50, blank=True)
    last_name = models.CharField(_("last name"), max_length=50, blank=True)
    middle_name = models.CharField(max_length=223, null=True, blank=True)
    email = models.EmailField(
        _("email address"),
    )

    photo = models.ImageField(upload_to="account/profile_pics/", blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    role = models.ForeignKey(Role, blank=True, null=True, on_delete=models.SET_NULL) # worker
    custom_uuid = models.UUIDField(unique=True, editable=False, null=True)
    father_phone = models.CharField(max_length=15, blank=True, null=True)
    mother_phone = models.CharField(max_length=15, blank=True, null=True)
    father_telegram_id = models.CharField(max_length=100, blank=True, null=True)
    mother_telegram_id = models.CharField(max_length=100, blank=True, null=True)
    
    start_work = models.DateField(blank=True, null=True)    
    
    is_worker = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone}"