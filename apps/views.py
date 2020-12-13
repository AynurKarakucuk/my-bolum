from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.db import models
from django.template import RequestContext

from apps.models import Personel
from apps.models import Duyuru
from apps.models import Etkinlik
from apps.models import Yonetici
from apps.models import AltSayfa
from apps.models import Banner

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.conf import settings

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.urls import reverse
from django.views import generic
from . import forms


"""
Admin Sayfaları başlangıç
"""
""" 
Login
"""
@login_required()
def sifre_view(request):

    if request.method == "POST":
        f = forms.YoneticiSifreForms(request.user, request.POST)
        if f.is_valid():
            f.save()

            return redirect('/yonetim/')
    else:
        f = forms.YoneticiSifreForms(request.user)

    context = {
        'baslik': 'MENU DÜZENLE',
        'form': f,
    }

    return render(request, 'admin/sifre.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)


            return redirect('/yonetim/')

    context = {
        "hata": True if request.POST else False,
    }

    return render(request, 'admin/login.html', context)


def logout_view(request):
    logout(request)

    return redirect('/login')


def admin_giris(request):
    return render(request, 'admin/ana_sayfa.html')


""" 
Login bitiş
"""

""" 
Personel admin
"""
@login_required
@permission_required('apps.view_personel', raise_exception=True)
def personel_detay(request, pk: int):
    personel = Personel.objects.get(id=pk)
    ck = CKEditorWidget().render('CV', personel.CV)

    context = {
        'personel': personel,
        'ck': ck,
    }
    return render(request, 'admin/personel/duzenle.html', context)

@login_required(login_url=settings.LOGIN_URL)
def personel_ekle2(request, pk: int = None):

    if request.method == 'POST':
        f = forms.PersonelForm(request.POST, request.FILES)

        if f.is_valid():
            personel = f.save(commit=False)
            personel.id = pk
            personel.save()

            return redirect('/yonetim/personel/')

    else:
        personel = Personel.objects.get(id=pk) if pk else None
        f = forms.PersonelForm(instance=personel)

    context = {
        'baslik': 'PERSONEL DÜZENLE' if pk else 'PERSONEL EKLE',
        'form': f,
    }

    return render(request, 'admin/personel/duzenle.html', context)



@login_required(login_url=settings.LOGIN_URL)
def personel_liste(request):
    personeller = Personel.objects.all()

    context = {'personeller': personeller}

    return render(request, 'admin/personel/liste.html', context)


@login_required(login_url=settings.LOGIN_URL)
def personel_sil(request, pk: int):
    personel = Personel.objects.get(id=pk)

    if request.method == 'POST':
        personel.delete()

        return redirect('/yonetim/personel/')
    else:
        context = {
            'personel': personel,
        }

    return render(request, 'admin/personel/sil.html', context)

@login_required(login_url=settings.LOGIN_URL)
def personel_detay(request, pk: int):
    personel = Personel.objects.get(id=pk)
    context = {
        'personel': personel,
    }

    return render(request, 'admin/personel/detay.html', context)
""" 
Personel son
"""

""" 
Duyurular admin
"""

@login_required
@permission_required('apps.view_personel', raise_exception=True)
def duyuru_detay(request, pk: int):
    duyuru = Duyuru.objects.get(id=pk)

    context = {
        'duyuru': duyuru,
    }

    return render(request, 'admin/duyuru/detay.html', context)

def duyuru_ekle2(request, pk: int = None):

    if request.method == 'POST':
        f = forms.DuyuruForm(request.POST, request.FILES)

        if f.is_valid():
            duyuru = f.save(commit=False)
            duyuru.id = pk
            duyuru.save()

            return redirect('/yonetim/duyuru/')

    else:
        duyuru = Duyuru.objects.get(id=pk) if pk else None
        f = forms.DuyuruForm(instance=duyuru)

    context = {
        'baslik': 'DUYURU DÜZENLE' if pk else 'DUYURU EKLE',
        'form': f,
    }

    return render(request, 'admin/duyuru/duzenle.html', context)


@login_required(login_url=settings.LOGIN_URL)
def duyuru_liste(request):
    duyuru = Duyuru.objects.all()

    context = {'duyuru': duyuru}

    return render(request, 'admin/duyuru/liste.html', context)


@login_required(login_url=settings.LOGIN_URL)
def duyuru_sil(request, pk: int):
    duyuru = Duyuru.objects.get(id=pk)

    if request.method == 'POST':
        duyuru.delete()

        return redirect('/yonetim/duyuru/')

    context = {
        'duyuru': duyuru,
    }

    return render(request, 'admin/duyuru/sil.html', context)


"""
Duyuru son
"""
"""
Haber Admin
"""

@login_required
@permission_required('apps.view_personel', raise_exception=True)
def haber_detay(request, pk: int):
    haber = Etkinlik.objects.get(id=pk)

    context = {
        'haber': haber,
    }

    return render(request, 'admin/haber/detay.html', context)

@login_required(login_url=settings.LOGIN_URL)
def haber_ekle2(request, pk: int = None):

    if request.method == 'POST':
        f = forms.EtkinlikForm(request.POST, request.FILES)

        if f.is_valid():
            haber = f.save(commit=False)
            haber.id = pk
            haber.save()

            return redirect('/yonetim/haber/')

    else:
        haber = Etkinlik.objects.get(id=pk) if pk else None
        f = forms.EtkinlikForm(instance=haber)

    context = {
        'baslik': 'ETKİNLİK DÜZENLE' if pk else 'ETKİNLİK EKLE',
        'form': f,
    }

    return render(request, 'admin/haber/duzenle.html', context)


@login_required(login_url=settings.LOGIN_URL)
def haber_liste(request):
    haber = Etkinlik.objects.all()

    context = {'haber': haber}

    return render(request, 'admin/haber/liste.html', context)


@login_required(login_url=settings.LOGIN_URL)
def haber_sil(request, pk: int):
    haber = Etkinlik.objects.get(id=pk)

    if request.method == 'POST':
        haber.delete()

        return redirect('/yonetim/haber/')

    context = {
        'haber': haber,
    }

    return render(request, 'admin/haber/sil.html', context)
"""
Haber Son
"""

"""
AltSayfalar
"""

@login_required
@permission_required('apps.view_personel', raise_exception=True)
def altsayfa_detay(request, pk: int):
    haber = AltSayfa.objects.get(id=pk)

    context = {
        'altsayfa': altsayfa,
    }

    return render(request, 'admin/altsayfa/detay.html', context)

@login_required(login_url=settings.LOGIN_URL)
def altsayfa_ekle2(request, pk: int = None):

    if request.method == 'POST':
        f = forms.AltSayfaForm(request.POST, request.FILES)

        if f.is_valid():
            altsayfa = f.save(commit=False)
            altsayfa.id = pk
            altsayfa.save()

            return redirect('/yonetim/altsayfa/')

    else:
        altsayfa = AltSayfa.objects.get(id=pk) if pk else None
        f = forms.AltSayfaForm(instance=altsayfa)

    context = {
        'baslik': 'ALT SAYFA DÜZENLE' if pk else 'ALT SAYFA EKLE',
        'form': f,
    }

    return render(request, 'admin/altsayfa/duzenle.html', context)


@login_required(login_url=settings.LOGIN_URL)
def altsayfa_liste(request):
    altsayfa = AltSayfa.objects.all()

    context = {'altsayfa': altsayfa}

    return render(request, 'admin/altsayfa/liste.html', context)


@login_required(login_url=settings.LOGIN_URL)
def altsayfa_sil(request, pk: int):
    altsayfa = AltSayfa.objects.get(id=pk)

    if request.method == 'POST':
        altsayfa.delete()

        return redirect('/yonetim/altsayfa/')

    context = {
        'altsayfa': altsayfa,
    }

    return render(request, 'admin/altsayfa/sil.html', context)
"""
Altsayfalar Son
"""
"""
Menu Admin
"""


@login_required
@permission_required('apps.view_personel', raise_exception=True)
def menu_detay(request, pk: int):
    menu = Banner.objects.get(id=pk)

    context = {
        'menu': menu,
    }

    return render(request, 'admin/menuler/duzenle.html', context)


@login_required(login_url=settings.LOGIN_URL)
def menu_ekle2(request, pk: int = None):

    if request.method == 'POST':
        f = forms.BannerForm(request.POST, request.FILES)

        if f.is_valid():
            menu = f.save(commit=False)
            menu.id = pk
            menu.save()

            return redirect('/yonetim/menu/')

    else:
        menu = Banner.objects.get(id=pk) if pk else None
        f = forms.BannerForm(instance=menu)

    context = {
        'baslik': 'MENU DÜZENLE' if pk else 'MENU EKLE',
        'form': f,
    }

    return render(request, 'admin/menuler/duzenle.html', context)



@login_required(login_url=settings.LOGIN_URL)
def menu_ekle(request, pk: int = None):
    # id var ise düzenleme
    if pk:
        menu = Banner.objects.get(id=pk)

    # id yok ise yeni kayıt
    else:
        menu = Banner()

    if request.method == 'POST':
        print(request.POST)
        menu.baslik = request.POST['baslik']
        #menu.icerik = request.POST['icerik']
        menu.alan = request.POST['alan1']
        menu.hedef = request.POST['hedef1']
        menu.durum = request.POST.get('durum', False)
        menu.save()
        return redirect('/yonetim/menu/')

    context = {
        'menu': menu,
    }

    return render(request, 'admin/menuler/duzenle.html', context)


@login_required(login_url=settings.LOGIN_URL)
def menu_liste(request):
    menu = Banner.objects.all()

    context = {'menu': menu}

    return render(request, 'admin/menuler/liste.html', context)



@login_required(login_url=settings.LOGIN_URL)
def menu_sil(request, pk: int):
    menu = Banner.objects.get(id=pk)

    if request.method == 'POST':
        menu.delete()

        return redirect('/yonetim/menu/')

    context = {
        'menu': menu,
    }

    return render(request, 'yonetim/menuler/sil.html', context)


"""
Menu Son
"""

"""
Kullanıcılar Admin
"""


@login_required
@permission_required('apps.view_personel', raise_exception=True)
def kullanici_detay(request, pk: int):
    kullanici = Yonetici.objects.get(id=pk)

    context = {
        'kullanici': kullanici,
    }

    return render(request, 'admin/kullanici/duzenle.html', context)


@login_required(login_url=settings.LOGIN_URL)
def kullanici_ekle(request, pk: int = None):
    # id var ise düzenleme
    if pk:
        kullanici = Yonetici.objects.get(id=pk)

    # id yok ise yeni kayıt
    else:
        kullanici = Yonetici()

    if request.method == 'POST':
        print(request.POST)
        kullanici.ad_soyad = request.POST['ad_soyad']
        kullanici.kullanici_adi = request.POST['kullanici_adi']
        kullanici.kullanici_sifre = request.POST['kullanici_sifre']
        kullanici.kullanici_yetki = request.POST['kullanici_yetki']
        kullanici.save()
        return redirect('/yonetim/kullanici/')

    context = {
        'kullanici': kullanici,
    }

    return render(request, 'admin/kullanici/duzenle.html', context)


@login_required(login_url=settings.LOGIN_URL)
def kullanici_ekle2(request, pk: int = None):

    if request.method == 'POST':
        f = forms.YoneticiForms(request.POST, request.FILES)

        if f.is_valid():
            kullanici = f.save(commit=False)
            kullanici.id = pk
            kullanici.save()

            return redirect('/yonetim/kullanici/')

    else:
        kullanici =Yonetici.objects.get(id=pk) if pk else None
        f = forms.YoneticiForms(instance=kullanici)

    context = {
        'baslik': 'MENU DÜZENLE' if pk else 'MENU EKLE',
        'form': f,
    }

    return render(request, 'admin/kullanici/duzenle.html', context)



def kullanici_kayit(request, pk: int = None):
    if request.method == "POST":
        f = forms.YoneticiForms(request.POST)
        if f.is_valid():
            f.save()

            return redirect('/yonetim/kullanici/')
    else:
        kullanici = User.objects.get(id=pk) if pk else None
        f = forms.YoneticiForms(instance=kullanici)

    context = {
        'baslik': 'MENU DÜZENLE' if pk else 'MENU EKLE',
        'form': f,
    }

    return render(request, 'admin/kullanici/duzenle.html', context)



#doktorlar_tum = Doktor.objects.filter(
#Q(first_name__contains=aranacak_kelime) | Q(last_name__contains=aranacak_kelime)
#)

@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_superuser, login_url=settings.YETKI_HATA_URL, redirect_field_name='')
def kullanici_liste(request):
    # xdkfldkjdkjkdjgkj
    kullanici = User.objects.all()

    context = {'kullanici': kullanici}

    return render(request, 'admin/kullanici/liste.html', context)


@login_required(login_url=settings.LOGIN_URL)
def kullanici_sil(request, pk: int):
    kullanici = Yonetici.objects.get(id=pk)

    if request.method == 'POST':
        kullanici.delete()

        return redirect('/yonetim/kullanici/')

    context = {
        'kullanici': kullanici,
    }

    return render(request, 'admin/kullanici/sil.html', context)

"""
Kullanıcılar Son
"""



"""
Admin Sayfaları bitiş
"""

"""
paydaş sayfaları
"""


def ana_sayfa(request):
    return render(request, 'anasayfa/ana_sayfa.html')


def hakkinda(request):
    return render(request, 'anasayfa/hakkinda.html')

