from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('homepage/', views.login, name='login'),
    path('reservasi/', views.reservasi, name='reservasi'),
    path('jadwal/<int:id>/', views.jadwal, name='jadwal'),
    path('hapus/<int:id>/', views.hapus, name='hapus'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/', views.update, name='update'),
    path('register/', views.register, name='register'), 
    path('daftar/', views.daftar, name='daftar'),
    path('admin/', views.admin, name='admin'),
    path('adminlog/', views.adminlog, name='adminlog'),
    path('terima/<int:id>/<int:admin>/', views.terima, name='terima'),
    path('tolak/<int:id>/<int:admin>/', views.tolak, name='tolak'),
]