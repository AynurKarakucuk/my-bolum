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

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.conf import settings

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator

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


@login_required
def admin_giris(request):
    return render(request, 'admin/ana_sayfa.html')


def logout_view(request):
    logout(request)

    return redirect('/login')


def yetki_yok(request):
    return render(request, 'admin/hata.html')


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
    personel = Personel.objects.get(id=pk) if pk else None

    if request.method == 'POST':
        f = forms.PersonelForm(request.POST, request.FILES, instance=personel)

        if f.is_valid():
            f.save()

            return redirect('/yonetim/personel/')

    else:

        f = forms.PersonelForm(instance=personel)

    context = {
        'baslik': 'PERSONEL DÜZENLE' if pk else 'PERSONEL EKLE',
        'form': f,
    }

    return render(request, 'admin/personel/duzenle.html', context)


@login_required(login_url=settings.LOGIN_URL)
def personel_liste(request):
    siralama = 'ad_soyad'

    sayfa = request.GET.get('sayfa', 1)

    personeller_tum = Personel.objects.order_by(siralama)
    paginator = Paginator(personeller_tum, 5)
    personeller = paginator.page(int(sayfa))
    # return render_to_response('doktor_listesi.html', locals())

    context = {
        'personeller': personeller
    }

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
def duyuru_detay(request, pk: int):
    duyuru = Duyuru.objects.get(id=pk)

    context = {
        'duyuru': duyuru,
    }

    return render(request, 'admin/duyuru/detay.html', context)


def duyuru_ekle2(request, pk: int = None):
    duyuru = Duyuru.objects.get(id=pk) if pk else None
    if request.method == 'POST':
        f = forms.DuyuruForm(request.POST, request.FILES, instance=duyuru)

        if f.is_valid():
            f.save()

            return redirect('/yonetim/duyuru/')

    else:

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
    dosya = True
    resim = True
    if duyuru.dosya is None: dosya = False
    if duyuru.resim is None: resim = False

    if request.method == 'POST':
        duyuru.delete()

        return redirect('/yonetim/duyuru/')

    context = {
        'duyuru': duyuru,
        'dosya': dosya,
        'resim': resim,
    }

    return render(request, 'admin/duyuru/sil.html', context)


"""
Duyuru son
"""
"""
Haber Admin
"""


@login_required
def haber_detay(request, pk: int):
    haber = Etkinlik.objects.get(id=pk)

    context = {
        'haber': haber,
    }

    return render(request, 'admin/haber/detay.html', context)


@login_required(login_url=settings.LOGIN_URL)
def haber_ekle2(request, pk: int = None):
    haber = Etkinlik.objects.get(id=pk) if pk else None

    if request.method == 'POST':
        f = forms.EtkinlikForm(request.POST, request.FILES, instance=haber)

        if f.is_valid():
            f.save()

            return redirect('/yonetim/haber/')

    else:
        f = forms.EtkinlikForm(instance=haber)

    context = {
        'baslik': 'ETKİNLİK ve HABER DÜZENLE' if pk else 'ETKİNLİK ve HABER EKLE',
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
def altsayfa_detay(request, pk: int):
    altsayfa = AltSayfa.objects.get(id=pk)

    context = {
        'altsayfa': altsayfa,
    }

    return render(request, 'admin/altsayfa/detay.html', context)


@login_required(login_url=settings.LOGIN_URL)
def altsayfa_ekle2(request, pk: int = None):
    altsayfa = AltSayfa.objects.get(id=pk) if pk else None
    if request.method == 'POST':
        f = forms.AltSayfaForm(request.POST, request.FILES, instance=altsayfa)

        if f.is_valid():
            f.save()

            return redirect('/yonetim/altsayfa/')

    else:

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


@login_required(login_url=settings.LOGIN_URL)
def menu_ekle2(request, pk: int = None):
    menu = Banner.objects.get(id=pk) if pk else None
    if request.method == 'POST':
        f = forms.BannerForm(request.POST, request.FILES, instance=menu)

        if f.is_valid():
            f.save()
            return redirect('/yonetim/menu/')

    else:
        f = forms.BannerForm(instance=menu)

    context = {
        'baslik': 'MENU DÜZENLE' if pk else 'MENU EKLE',
        'form': f,
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
def kullanici_detay(request, pk: int):
    kullanici = User.objects.get(id=pk)

    context = {
        'kullanici': kullanici,
    }

    return render(request, 'admin/kullanici/duzenle.html', context)


def kullanici_kayit(request, pk: int = None):
    kullanici = User.objects.get(id=pk) if pk else None
    if request.method == "POST":
        f = forms.YoneticiForms(request.POST)
        if f.is_valid():
            f.save()

            return redirect('/yonetim/kullanici/')
    else:

        f = forms.YoneticiForms(instance=kullanici)

    context = {
        'baslik': 'MENU DÜZENLE' if pk else 'MENU EKLE',
        'form': f,
    }

    return render(request, 'admin/kullanici/duzenle.html', context)


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_superuser, login_url=settings.YETKI_HATA_URL, redirect_field_name='')
def kullanici_liste(request):
    # xdkfldkjdkjkdjgkj
    kullanici = User.objects.all()

    context = {'kullanici': kullanici}

    return render(request, 'admin/kullanici/liste.html', context)


@login_required(login_url=settings.LOGIN_URL)
def kullanici_sil(request, pk: int):
    kullanici = User.objects.get(id=pk)

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

"""  ANASAYFA Vieww Komutları"""


def altsayfa_goster(request, baslik, pk: int):
    bilgi = AltSayfa.objects.filter(id=pk, durum=True).first()

    if bilgi is None:
        context = {'baslik': "Güncelleniyor",
                   'bilgi': bilgi,
                   }

        return render(request, 'anasayfa/iletisim.html', context)
    else:

        context = {
            'bilgi': bilgi,
            'baslik': baslik,
            # 'post.title': alan,
        }
        return render(request, 'anasayfa/iletisim.html', context)


def iletisim(request):
    bilgi = AltSayfa.objects.filter(alan="iletisim").first()
    return altsayfa_goster(request, "İLETİŞİM", bilgi.id)


def misyon(request):
    bilgi = AltSayfa.objects.filter(alan="misyon_vizyon").first()
    return altsayfa_goster(request, "MİSYON VİZYON", bilgi.id)


def hakkinda(request):
    bilgi = AltSayfa.objects.filter(alan="hakkinda").first()
    return altsayfa_goster(request, "HAKKINDA", bilgi.id)


def genel_bilgi(request):
    bilgi = AltSayfa.objects.filter(alan="genelbilgi").first()

    return altsayfa_goster(request, "Genel Bilgi", bilgi.id)


def ogretim_plani(request):
    bilgi = AltSayfa.objects.filter(alan="ogretim_plani").first()
    return altsayfa_goster(request, "Öğretim Planı", bilgi.id)


def ders_icerik(request):
    bilgi = AltSayfa.objects.filter(alan="ders_icerik").first()
    return altsayfa_goster(request, "Ders İçerikleri", bilgi.id)


def bilgi_sistemi(request):
    bilgi = AltSayfa.objects.filter(alan="ogrenci_sistemi").first()
    return altsayfa_goster(request, "Öğrenci Bilgi Sistemi", bilgi.id)


def formlar_icerik(request):
    bilgi = AltSayfa.objects.filter(baslik="Formlar").first()

    return altsayfa_goster(request, "Formlar", bilgi.id)


def otomasyon_icerik(request):
    bilgi = AltSayfa.objects.filter(baslik="Öğrenci Otomasyon").first()
    return altsayfa_goster(request, "Öğrenci Otomasyon", bilgi.id)


def belgeler_icerik(request):
    bilgi = AltSayfa.objects.filter(baslik="Belgeler", ).first()
    return altsayfa_goster(request, "Belgeler", bilgi.id)


def idari_personel(request, pk: int = None):
    if pk:
        bilgi = Personel.objects.get(id=pk)
        context = {'bilgi': bilgi}
        return render(request, 'anasayfa/detay_personel.html', context)
    else:
        bilgi = Personel.objects.filter(kategori='İdari', durum=True)
        if bilgi is None:
            context = {'baslik': "güncelleniyor"}

            return render(request, 'anasayfa/personel.html', context)

        context = {
            'bilgi': bilgi,
            'baslik': "İdari Personeller",
            'post.title': "idari",
        }
        return render(request, 'anasayfa/personel.html', context)


def akademik_personel(request, pk: int = None):
    if pk:
        bilgi = Personel.objects.get(id=pk)
        context = {'bilgi': bilgi}
        return render(request, 'anasayfa/detay_personel.html', context)
    else:
        bilgi = Personel.objects.filter(kategori='Akademik', durum=True)
        if bilgi is None:
            context = {'baslik': "güncelleniyor"}
            return render(request, 'anasayfa/personel.html', context)

        context = {
            'bilgi': bilgi,
            'baslik': "Akademik Personeller",
            'post.title': "akademik",
        }
        return render(request, 'anasayfa/personel.html', context)


def haber_goster(request, pk: int = None):
    if pk:
        bilgi = Etkinlik.objects.get(id=pk)
        context = {
            'bilgi': bilgi,
            'veri': "haber",
        }
        return render(request, 'anasayfa/detay_duyuru_haber.html', context)
    else:
        bilgi1 = Etkinlik.objects.filter(durum=True)
        bilgi = bilgi1.order_by('tarih')

        context = {
            'bilgi': bilgi,
            'baslik': "Etkinlik ve Haberler",
            'veri': "haber",
        }
        return render(request, 'anasayfa/haber_goster.html', context)


def duyuru_goster(request, pk: int = None):
    if pk:
        bilgi = Duyuru.objects.get(id=pk)
        context = {
            'bilgi': bilgi,
            'veri': "duyuru",
        }
        return render(request, 'anasayfa/detay_duyuru_haber.html', context)
    else:
        bilgi = Duyuru.objects.filter(durum=True)
        bilgi = bilgi.order_by('tarih')
        context = {
            'bilgi': bilgi,
            'baslik': "Duyurular",
            'veri': "duyuru",
        }
        return render(request, 'anasayfa/haber_goster.html', context)


def ana_sayfa(request):
    sayfa = request.GET.get('sayfa', 1)

    bilgi1 = Etkinlik.objects.filter(durum=True)
    etkinlik_tum = bilgi1.order_by('tarih')
    paginator = Paginator(etkinlik_tum, 3)
    haber = paginator.page(int(sayfa))

    bilgi2 = Duyuru.objects.filter(durum=True)
    duyuru_tum = bilgi2.order_by('tarih')
    paginator_duyuru = Paginator(duyuru_tum, 3)
    duyuru = paginator_duyuru.page(int(sayfa))
    context = {
        'haber': haber,
        'duyuru': duyuru,
    }
    return render(request, 'anasayfa/ana_sayfa.html', context)
