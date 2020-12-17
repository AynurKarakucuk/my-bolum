from django.db import models
from ckeditor.fields import RichTextField


class Banner(models.Model):
    id = models.IntegerField(primary_key=True)
    baslik = models.CharField(max_length=100)
    alan = models.CharField(max_length=100,blank=True, null=True,)
    durum = models.BooleanField(blank=True, null=True, verbose_name='Aktif')


class AltSayfa(models.Model):
    id = models.IntegerField(primary_key=True)
    baslik = models.CharField(max_length=100, verbose_name='Başlık')
    icerik = RichTextField(verbose_name="içerik", null=True, blank=True)
    alan = models.CharField(max_length=100)
    hedef = models.URLField()
    durum = models.BooleanField(blank=True, null=True, verbose_name='Aktif')
    dosya = models.FileField(blank=True, null=True, )


class Etkinlik(models.Model):
    id = models.IntegerField(primary_key=True)
    baslik = models.CharField(max_length=100, verbose_name='Başlık')
    icerik = RichTextField(verbose_name="içerik", null=True, blank=True)
    resim = models.ImageField(blank=True, null=True, )
    tarih = models.DateTimeField()
    dosya = models.FileField(blank=True, null=True, )
    durum = models.BooleanField(blank=True, null=True, verbose_name='Aktif')


class Duyuru(models.Model):
    id = models.IntegerField(primary_key=True)
    tarih = models.DateTimeField()
    baslik = models.CharField(max_length=100, verbose_name='Başlık')
    icerik = RichTextField(verbose_name="içerik", null=True, blank=True)
    durum = models.BooleanField(blank=True, null=True, verbose_name='Aktif')
    dosya = models.FileField(blank=True, null=True, )
    resim = models.ImageField(blank=True, null=True, )


class Personel(models.Model):
    id = models.IntegerField(primary_key=True)
    kategori = models.CharField(max_length=50)
    unvan = models.CharField(max_length=50, verbose_name='abc')
    ad_soyad = models.CharField(max_length=50, verbose_name='Adı Soyadı')
    resim = models.FileField(upload_to='uploads/', null=True, blank=True)
    CV = RichTextField(verbose_name='Öz Geçmiş', null=True, blank=True)
    durum = models.BooleanField(blank=True, null=True, verbose_name='Aktif')

    def __str__(self):
        return self.ad_soyad


class Yonetici(models.Model):
    id = models.IntegerField(primary_key=True)
    ad_soyad = models.CharField(max_length=50, verbose_name='Adı Soyadı')
    kullanici_adi = models.CharField(max_length=50, verbose_name='Kullanıcı Adı')
    kullanici_sifre = models.CharField(max_length=50, verbose_name='Kullanıcı Şifre')
    kullanici_yetki = models.CharField(max_length=50, verbose_name='Kullanıcı Yetki')
