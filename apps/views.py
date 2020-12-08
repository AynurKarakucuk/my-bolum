from django.shortcuts import render
from django.db import models
from apps.models import Personel
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.conf import settings

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout

"""
Admin Sayfaları başlangıç
"""


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('/yonetim/')

    context = {
        "hata": True if request.POST else False
    }

    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)

    return redirect('/login')


def admin_giris(request):
    return render(request, 'admin/ana_sayfa.html')


@login_required
@permission_required('apps.view_personel', raise_exception=True)
def personel_detay(request, pk: int):
    personel = Personel.objects.get(id=pk)

    context = {
        'personel': personel,
    }

    return render(request, 'admin/personel/duzenle.html', context)


@login_required(login_url=settings.LOGIN_URL)
def personel_ekle(request, pk: int = None):
    # id var ise düzenleme
    if pk:
        personel = Personel.objects.get(id=pk)

    # id yok ise yeni kayıt
    else:
        personel = Personel()

    if request.method == 'POST':
        print(request.POST)
        personel.ad_soyad = request.POST['ad_soyad']
        personel.kategori = request.POST['kategori']
        personel.unvan = request.POST['unvan']
        personel.resim = request.POST['resim']
        personel.durum = request.POST.get('durum', False)
        personel.CV = request.POST['CV']
        personel.save()
        return redirect('/yonetim/personel/')

    context = {
        'personel': personel,
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

    context = {
        'personel': personel,
    }

    return render(request, 'admin/personel/sil.html', context)


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
