from __future__ import absolute_import

from django import forms
from ckeditor_uploader.fields import RichTextUploadingFormField
from datetimewidget.widgets import DateTimeWidget
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User

from apps.models import Personel, Duyuru, Etkinlik, Yonetici, AltSayfa, Banner

""" Personel Form"""


class PersonelForm(forms.ModelForm):
    CV = RichTextUploadingFormField(
        config_name="my-custom-toolbar",
        label="Öz Geçmiş",
        required=False,

    )
    # resim = forms.FileField()
    kategori = forms.ChoiceField(
        choices=[
            ("İdari", "İdari"),
            ("Akademik", "Akademik"),
        ],

    )
    unvan = forms.ChoiceField(
        choices=[
            ("Prof.Dr.", "Prof.Dr."),
            ("Doç.", "Doç."),
            ("Dr.Öğr.Gör.", "Dr.Öğr.Gör."),
            ("Öğr.Gör.", "Öğr.Gör."),
            ("Uzman", "Uzman"),
            ("Tekniker", "Tekniker"),
            ("Memur", "Memur"),
        ]

    )
    durum = forms.BooleanField(required=False, label="Aktif")

    class Meta:
        model = Personel
        fields = ['kategori', 'unvan', 'ad_soyad', 'resim', 'CV', 'durum']


""" Etkinlik Form"""


class EtkinlikForm(forms.ModelForm):
    icerik = RichTextUploadingFormField(
        config_name="my-custom-toolbar",
        required=False,
    )

    durum = forms.BooleanField(required=False, label="Aktif")

    class Meta:
        model = Etkinlik
        fields = ['tarih', 'baslik', 'icerik', 'durum', 'resim', 'dosya']
        widgets = {
            'tarih': DateTimeWidget(attrs={'id': "yourdatetimeid"}, usel10n=True, bootstrap_version=3)
        }


class DuyuruForm(forms.ModelForm):
    icerik = RichTextUploadingFormField(
        config_name="my-custom-toolbar",
        required=False,
    )

    durum = forms.BooleanField(required=False, label="Aktif")

    class Meta:
        model = Duyuru
        fields = ['tarih', 'baslik', 'icerik', 'durum', 'dosya', 'resim']
        widgets = {
            'tarih': DateTimeWidget(attrs={'id': "yourdatetimeid"}, usel10n=True, bootstrap_version=3)
        }

""" Alt Sayfalar Form"""


class AltSayfaForm(forms.ModelForm):
    icerik = RichTextUploadingFormField(
        config_name="my-custom-toolbar",
        required=False,

    )
    alan = forms.ChoiceField(
        choices=[
            ("hakkinda", "Hakkında"),
            ("misyon_vizyon", "Misyon Vizyon"),
            ("iletisim", "İletişim"),
            ("anasayfa", "Ana Sayfa"),
            ("idari", "İdari"),
            ("akademik", "Akademik"),
            ("genelbilgi", "Genel Bilgi"),
            ("ogretim_plani", "Öğretim Planı"),
            ("ders_icerik", "Ders İçerikleri"),
            ("ogrenci_sistemi", "Öğrenci Bilgi Sistemi"),
        ],

    )

    durum = forms.BooleanField(required=False, label="Aktif")

    class Meta:
        model = AltSayfa
        fields = ['baslik', 'alan', 'icerik', 'durum', 'dosya']

""" Menu Form"""

class BannerForm(forms.ModelForm):

    durum = forms.BooleanField(required=False, label="Aktif")

    class Meta:
        model = Banner
        fields = ['baslik', 'durum', 'alan']


class YoneticiForms(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')

class YoneticiSifreForms(PasswordChangeForm):
    pass
    # class Meta:
    #     model = User
    #     fields = ()

class AdminSifreResetForms(SetPasswordForm):
    pass

