from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.conf import settings



class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(email=email, **kwargs)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email, password=password, **kwargs)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    recepient_name = models.CharField(max_length=255, verbose_name='Recipient name', null=False, blank=False)
    postal_code = models.CharField(max_length=20, verbose_name='Postal code', blank=False, null=False)
    administrative_area = models.CharField(max_length=20, verbose_name='Administrative area', blank=True, null=False, default='')
    locality = models.CharField(max_length=255, verbose_name='City/town', blank=True, null=False, default='')
    address_line = models.CharField(max_length=255, verbose_name='Street number and name', null=False, blank=False)
    company = models.CharField(max_length=255, verbose_name="Company", null=True, blank=True)
    additional_info = models.CharField(max_length=255, verbose_name='Additional information', null=True, blank=True)

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=255, unique=True, blank=False, verbose_name="Email"
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserAccountManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email



