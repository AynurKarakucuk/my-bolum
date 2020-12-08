from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
from django.db.models import IntegerField
from django.utils import timezone

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    baslik = models.CharField(max_length=50, verbose_name="Title")
    icerik = models.CharField(max_length=50)
    alan = models.CharField(max_length=50)
    hedef = models.URLField()
    durum = models.BooleanField()


class AltSayfa(models.Model):
    id = models.IntegerField(primary_key=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    baslik = models.CharField(max_length=50)
    icerik = models.CharField(max_length=50)
    alan = models.CharField(max_length=50)
    hedef = models.URLField()
    durum = models.BooleanField()


class Etkinlik(models.Model):
    id = models.IntegerField(primary_key=True)
    baslik = models.CharField(max_length=50)
    icerik = models.CharField(max_length=50)
    resim = models.ImageField()
    tarih = models.DateTimeField()
    durum = models.BooleanField()


class Duyuru(models.Model):
    id = models.IntegerField(primary_key=True)
    tarih = models.DateTimeField()
    baslik = models.CharField(max_length=50)
    icerik = models.CharField(max_length=50)
    durum = models.BooleanField()


class Banner(models.Model):
    id = models.IntegerField(primary_key=True)
    baslik = models.CharField(max_length=50)
    resim = models.ImageField()
    durum = models.BooleanField()


class Personel(models.Model):
    id = models.IntegerField(primary_key=True)
    kategori = models.CharField(max_length=50)
    unvan = models.CharField(max_length=50)
    ad_soyad = models.CharField(max_length=50)
    resim = models.ImageField()
    CV = models.CharField(max_length=1000)
    durum = models.BooleanField(blank=True, null=True)


class Yonetici(models.Model):
    id = models.IntegerField(primary_key=True)
    ad_soyad = models.CharField(max_length=50)
    kullanici_ad_soyad = models.CharField(max_length=50)
    kullanici_adi = models.CharField(max_length=50)
    kullanici_sifre = models.CharField(max_length=50)
    kullanici_yetki = models.CharField(max_length=50)
