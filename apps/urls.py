from django.urls import path
from django.conf.urls import*
from . import views


urlpatterns = [
    # path('articles/', views.year_archive),
    # path('articles/<int:year>/', views.year_archive),
    # path('articles/<int:year>/<int:month>/', views.month_archive),
    # path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('articles/', views.personel_liste),
    path('articles/<int:pk>/', views.personel_detay),
    path('articles/edit', views.personel_ekle),
    path('articles/edit/<int:pk>/', views.personel_ekle),
    path('articles/delete/<int:pk>/', views.personel_sil),
    path('', views.ana_sayfa),
    path('hakkinda/', views.hakkinda),


    # url(r'^personel/', include('delete.html')),
]