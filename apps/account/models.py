from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator


class CustomUser(AbstractUser):
    
    phone = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(_("first name"), max_length=50, blank=True)
    last_name = models.CharField(_("last name"), max_length=50, blank=True)
    email = models.EmailField(
        _("email address"),
    )

    photo = models.ImageField(upload_to="account/profile_pics/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    custom_uuid = models.UUIDField(unique=True, editable=False, null=True)
    father_phone = models.CharField(max_length=15, blank=True, null=True)
    mother_phone = models.CharField(max_length=15, blank=True, null=True)
    father_telegram_id = models.CharField(max_length=100, blank=True, null=True)
    mother_telegram_id = models.CharField(max_length=100, blank=True, null=True)
    
    is_archived = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone}"