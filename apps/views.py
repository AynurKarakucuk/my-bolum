from django.shortcuts import render
from django.db import models
from apps.models import Personel
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.conf import settings

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout


def year_archive(request):
    """

    if request.method == "POST":
    elif request.method == "GET":
    elif request.method == "DELETE":
    """

    a_list = [
        {"ad": "ali", "not": 1},
        {"ad": "veli", "not": 2},
    ]

    context = {'year': 2012, 'article_list': a_list, "menu": ""}

    return render(request, 'sayfa/list.html', context)


@login_required
@permission_required('apps.view_personel', raise_exception=True)
def personel_detay(request, pk: int):
    personel = Personel.objects.get(id=pk)

    context = {
        'year': 1,
        'personel': personel,
        'menu': ''
    }

    return render(request, 'sayfa/edit.html', context)


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
        return redirect('/articles/')

    context = {
        'personel': personel,
    }

    return render(request, 'sayfa/edit.html', context)


@login_required(login_url=settings.LOGIN_URL)
def personel_liste(request):
    personeller = Personel.objects.all()

    context = {'personeller': personeller}

    return render(request, 'sayfa/list.html', context)


@login_required(login_url=settings.LOGIN_URL)
def personel_sil(request, pk: int):
    personel = Personel.objects.get(id=pk)

    if request.method == 'POST':
        personel.delete()

        return redirect('/articles/')

    context = {
        'personel': personel,
    }

    return render(request, 'sayfa/delete.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('/articles/')

    context = {
        "hata": True if request.POST else False
    }

    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)

    return redirect('/login')


def ana_sayfa(request):
    return render(request, 'anasayfa/ana_sayfa.html')


def hakkinda(request):
    return render(request, 'anasayfa/hakkinda.html')
