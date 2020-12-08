from django.urls import path
from django.conf.urls import*
from . import views


urlpatterns = [
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('yonetim/personel/', views.personel_liste),
    path('yonetim/personel/<int:pk>/', views.personel_detay),
    path('yonetim/personel/duzenle', views.personel_ekle),
    path('yonetim/personel/duzenle/<int:pk>/', views.personel_ekle),
    path('yonetim/personel/sil/<int:pk>/', views.personel_sil),
    path('', views.ana_sayfa),
    path('hakkinda/', views.hakkinda),
    path('yonetim/', views.admin_giris),


    # url(r'^duyuru/', include('delete.html')),
]
