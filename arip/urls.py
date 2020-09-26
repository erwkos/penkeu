from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'arip'

urlpatterns = [
    # page duta
    path('', views.dashboardduta, name='dashboardduta'),
    path('upload/buktibayar/', views.uploadbuktibayar, name='uploadbuktibayar'),
    path('laporan/buktibayar/', views.laporanbuktibayar, name='laporanbuktibayar'),
    path('upload/ba/rekonsiliasi/', views.uploadbarekonsiliasi, name='uploadbarekonsiliasi'),
    path('laporan/ba/rekonsiliasi/', views.laporanbarekonsiliasi, name='laporanbarekonsiliasi'),
    path('riwayat/perubahan/', views.history, name='history'),

    # page pegawai
    path('dashboard/SKPD/', views.dashboardSKPD, name='dashboardSKPD'),
    path('datapegawai/', views.datapegawai, name='datapegawai'),
    path('update/pegawai/<int:id>/', views.updatepegawai, name='updatepegawai'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)