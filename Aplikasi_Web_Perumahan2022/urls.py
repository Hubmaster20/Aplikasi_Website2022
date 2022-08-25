"""Aplikasi_Web_Perumahan2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from Aplikasi_Web_Perumahan2022 import settings
from django.urls import path
# from django.contrib.auth import views
from django.contrib import admin
from . import views
from .views import index, HomeView, LogoutView, Data_kategori_perumahan, Tambah_kategori_perumahan, Edit_kategori_perumahan, Hapus_kategori_perumahan, Data_vasilitas_perumahan, Tambah_vasilitas_perumahan, Edit_vasilitas_perumahan, Hapus_vasilitas_perumahan, Data_perumahan, Tambah_perumahan, Edit_perumahan, Hapus_perumahan, Data_kategori_kosan, Tambah_kategori_kosan, Edit_kategori_kosan, Hapus_kategori_kosan, Data_vasilitas_kosan, Tambah_vasilitas_kosan, Edit_vasilitas_kosan, Hapus_vasilitas_kosan, Data_kosan, Tambah_kosan, Edit_kosan, Hapus_kosan, Halaman_kosan, cari_kosan, detail_kosan, cari_vasilitas_kosan, cari_perumahan, detail_perumahan, cari_vasilitas_perumahan, LP_perumahan, LP_kosan

urlpatterns = [
    url(r'^$',index, name="index"),
    url(r'^Home/$', HomeView, name="Home"),
    url(r'^logout/$',LogoutView, name="logout"),
    # kategori perumahan
    url(r'^Kategori_perumahan/$',Data_kategori_perumahan, name="Kategori_perumahan"),
    url(r'^Tambah_kategori_perumahan/$',Tambah_kategori_perumahan, name="Tambah_kategori_perumahan"),
    url(r'^hapus_kategori_perumahan/(?P<hapus_kr>[0-9]+)$',Hapus_kategori_perumahan, name="hapus_kategori_perumahan"),
    url(r'^edit_kategori_perumahan/(?P<id_kr>[0-9]+)$',Edit_kategori_perumahan, name="edit_kategori_perumahan"),
    # vasilitas
    url(r'^Vasilitas_perumahan/$',Data_vasilitas_perumahan, name="Vasilitas_perumahan"),
    url(r'^Tambah_vasilitas_perumahan/$',Tambah_vasilitas_perumahan, name="Tambah_vasilitas_perumahan"),
    url(r'^hapus_vasilitas_perumahan/(?P<hapus_vsp>[0-9]+)$',Hapus_vasilitas_perumahan, name="hapus_vasilitas_perumahan"),
    url(r'^edit_vasilitas_perumahan/(?P<id_vsp>[0-9]+)$',Edit_vasilitas_perumahan, name="edit_vasilitas_perumahan"),
    # perumahan
    url(r'^Perumahan/$',Data_perumahan, name="Perumahan"),
    url(r'^Tambah_perumahan/$',Tambah_perumahan, name="Tambah_perumahan"),
    url(r'^hapus_perumahan/(?P<hapus_pr>[0-9]+)$',Hapus_perumahan, name="hapus_perumahan"),
    url(r'^edit_perumahan/(?P<id_pr>[0-9]+)$',Edit_perumahan, name="edit_perumahan"),
    # kategori kosan
    url(r'^Kategori_kosan/$',Data_kategori_kosan, name="Kategori_kosan"),
    url(r'^Tambah_kategori_kosan/$',Tambah_kategori_kosan, name="Tambah_kategori_kosan"),
    url(r'^hapus_kategori_kosan/(?P<hapus_ks>[0-9]+)$',Hapus_kategori_kosan, name="hapus_kategori_kosan"),
    url(r'^edit_kategori_kosan/(?P<id_ks>[0-9]+)$',Edit_kategori_kosan, name="edit_kategori_kosan"),
    # vasilitas kosan
    url(r'^Vasilitas_kosan/$',Data_vasilitas_kosan, name="Vasilitas_kosan"),
    url(r'^Tambah_vasilitas_kosan/$',Tambah_vasilitas_kosan, name="Tambah_vasilitas_kosan"),
    url(r'^hapus_vasilitas_kosan/(?P<hapus_ksn>[0-9]+)$',Hapus_vasilitas_kosan, name="hapus_vasilitas_kosan"),
    url(r'^edit_vasilitas_kosan/(?P<id_ksn>[0-9]+)$',Edit_vasilitas_kosan, name="edit_vasilitas_kosan"),
    # membuat laporan
    url(r'^LP_perumahan/$',LP_perumahan, name="LP_perumahan"),
    url(r'^LP_kosan/$',LP_kosan, name="LP_kosan"),
    # kosan
    url(r'^Kosan/$',Data_kosan, name="Kosan"),
    url(r'^Tambah_kosan/$',Tambah_kosan, name="Tambah_kosan"),
    url(r'^hapus_kosan/(?P<hapus_ksn>[0-9]+)$',Hapus_kosan, name="hapus_kosan"),
    url(r'^edit_kosan/(?P<id_ksn>[0-9]+)$',Edit_kosan, name="edit_kosan"),
    # halaman kosan
    url(r'^WEBSITE/$',Halaman_kosan, name="Halaman_kosan"),
    url(r'^cari_kosan/$',cari_kosan, name="cari_kosan"),
    url(r'^detail_kosan/$',detail_kosan, name="detail_kosan"),
    url(r'^cari_vasilitas_kosan/$',cari_vasilitas_kosan, name="cari_vasilitas_kosan"),
    # halaman perumahan atau cari data
    url(r'^cari_perumahan/$',cari_perumahan, name="cari_perumahan"),
    url(r'^detail_perumahan/$',detail_perumahan, name="detail_perumahan"),
    url(r'^cari_vasilitas_perumahan/$',cari_vasilitas_perumahan, name="cari_vasilitas_perumahan"),


    path('admin/', admin.site.urls),
]


if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)