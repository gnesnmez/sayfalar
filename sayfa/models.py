from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    sifre = models.CharField(max_length=100)
    rutbe = models.CharField(max_length=20, default='uye')
    dogum_tarihi = models.DateField()
    cinsiyet = models.CharField(max_length=10)
    telefon = models.CharField(max_length=20)

    class Meta:
        swappable = 'AUTH_USER_MODEL'


# Geriye dönük adları değiştir
User.groups.related_name = 'custom_user_groups'
User.user_permissions.related_name = 'custom_user_permissions'

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)

class Egitmen(models.Model):
    egitmen_id = models.AutoField(primary_key=True)
    telefon = models.CharField(max_length=20)
    dogum_tarihi = models.DateField()
    cinsiyet = models.CharField(max_length=10)
    ilgi_alani = models.TextField()
