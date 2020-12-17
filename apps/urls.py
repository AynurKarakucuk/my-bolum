from django.urls import path
from django.conf.urls import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = (
        [
            path('login/', views.login_view),
            path('logout/', views.logout_view),
            # """ Personel Sayfası"""
            path('yonetim/personel/', views.personel_liste),
            path('yonetim/personel/<int:pk>/', views.personel_detay),
            path('yonetim/personel/duzenle', views.personel_ekle2),
            path('yonetim/personel/duzenle/<int:pk>/', views.personel_ekle2),
            path('yonetim/personel/sil/<int:pk>/', views.personel_sil),
            path('yonetim/personel/detay/<int:pk>/', views.personel_detay),
            # """Duyuru Sayfası"""
            path('yonetim/duyuru/', views.duyuru_liste),
            path('yonetim/duyuru/<int:pk>/', views.duyuru_detay),
            path('yonetim/duyuru/duzenle', views.duyuru_ekle2),
            path('yonetim/duyuru/duzenle/<int:pk>/', views.duyuru_ekle2),
            path('yonetim/duyuru/sil/<int:pk>/', views.duyuru_sil),
            path('yonetim/duyuru/detay/<int:pk>/', views.duyuru_detay),
            # """Etkinlik Sayfası"""
            path('yonetim/haber/', views.haber_liste),
            path('yonetim/haber/<int:pk>/', views.haber_detay),
            path('yonetim/haber/duzenle', views.haber_ekle2),
            path('yonetim/haber/duzenle/<int:pk>/', views.haber_ekle2),
            path('yonetim/haber/sil/<int:pk>/', views.haber_sil),
            path('yonetim/haber/detay/<int:pk>/', views.haber_detay),
            # """ Alt Sayfalar """
            # """Etkinlik Sayfası"""
            path('yonetim/altsayfa/', views.altsayfa_liste),
            path('yonetim/altsayfa/<int:pk>/', views.altsayfa_detay),
            path('yonetim/altsayfa/duzenle', views.altsayfa_ekle2),
            path('yonetim/altsayfa/duzenle/<int:pk>/', views.altsayfa_ekle2),
            path('yonetim/altsayfa/sil/<int:pk>/', views.altsayfa_sil),
            path('yonetim/altsayfa/detay/<int:pk>/', views.altsayfa_detay),
            # """ Menu Sayfası """
            path('yonetim/menu/', views.menu_liste),
            path('yonetim/menu/duzenle', views.menu_ekle2),
            path('yonetim/menu/duzenle/<int:pk>/', views.menu_ekle2),
            path('yonetim/menu/sil/<int:pk>/', views.menu_sil),
            # """ Kullanıcılar """
            path('yonetim/kullanici/', views.kullanici_liste),
            path('yonetim/kullanici/<int:pk>/', views.kullanici_detay),
            path('yonetim/kullanici/duzenle', views.kullanici_kayit),
            path('yonetim/kullanici/duzenle/<int:pk>/', views.kullanici_kayit),
            path('yonetim/kullanici/sil/<int:pk>/', views.kullanici_sil),
            path('yonetim/kullanici/detay/<int:pk>/', views.kullanici_detay),

            # YÖNETİM GİRİŞ
            path('yonetim/', views.admin_giris),
            path('sifre/', views.sifre_view),
            path('hata_yetki/', views.yetki_yok),

            # ANA SAYFA
            path('', views.ana_sayfa),
            path('hakkinda/', views.hakkinda),
            path('iletisim/', views.iletisim),
            path('misyon_vizyon/', views.misyon),
            path('genel_bilgi/', views.genel_bilgi),
            path('ogretim_plani/', views.ogretim_plani),
            path('ders_icerik/', views.ders_icerik),
            path('bilgi_sistemi/', views.bilgi_sistemi),
            path('idari_personel/', views.idari_personel),
            path('idari_personel/<int:pk>/', views.idari_personel),
            path('akademik_personel/', views.akademik_personel),
            path('akademik_personel/<int:pk>/', views.akademik_personel),
            path('formlar/', views.formlar_icerik),
            path('otomasyon/', views.otomasyon_icerik),
            path('belgeler/', views.belgeler_icerik),
            path('haber_goster/', views.haber_goster),
            path('duyuru_goster/', views.duyuru_goster),
            path('haber_goster/<int:pk>/', views.haber_goster),
            path('duyuru_goster/<int:pk>/', views.duyuru_goster),


            path('ckeditor/', include('ckeditor_uploader.urls')),

        ]
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
