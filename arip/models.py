from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils.functional import cached_property
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from simple_history.models import HistoricalRecords

CHOICES_STATUS_PEGAWAI = [
    ('Aktif', 'Aktif'),
    ('Meninggal', 'Meninggal'),
    ('Pensiun', 'Pensiun'),
    ('Diberhentikan', 'Diberhentikan')
]

CHOICES_STATUS_PEMDA = [
    ('Provinsi Sumatera Utara', 'Provinsi Sumatera Utara'),
    ('Kota Medan', 'Kota Medan'),
    ('Kota Binjai', 'Kota Binjai'),
    ('Kabupaten Langkat', 'Kabupaten Langkat')
]

CHOICES_JENIS_IURAN = [
    ('Iuran 1%', 'Iuran 1%'),
    ('Iuran 4%', 'Iuran 4%'),
]


class BayarTagihan(models.Model):
    bulan_tagihan = models.DateField()
    tanggal_bayar = models.DateField()
    nominal_bayar = models.BigIntegerField(default=0)
    ntpn = models.CharField(max_length=50)
    kode_akun = models.CharField(max_length=50)
    jenis_iuran = models.CharField(max_length=50, choices=CHOICES_JENIS_IURAN)
    file_buktibayar = models.FileField(upload_to='documents/', blank=True, null=True)
    history = HistoricalRecords()


class Rekonsiliasi(models.Model):
    bulan_tagihan = models.DateField()
    tanggal_rekonsilisasi = models.DateField()
    no_ba_rekonsiliasi_pemda = models.CharField(max_length=50)
    no_ba_rekonsiliasi_bpjs_kesehatan = models.CharField(max_length=50)
    file_ba_rekonsiliasi = models.FileField(upload_to='documents/', blank=True, null=True)
    history = HistoricalRecords()


class SKPD(models.Model):
    nama_skpd = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_skpd


class DataPegawai(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    pemda = models.CharField(max_length=50, choices=CHOICES_STATUS_PEMDA)
    nmsatker = models.CharField(max_length=100, blank=True, null=True)
    nmskpd = models.CharField(max_length=100)
    tglgaji = models.DateField()
    nama = models.CharField(max_length=100)
    nip = models.CharField(max_length=20)
    noktp = models.CharField(max_length=25, blank=True, null=True)
    jistri = models.PositiveIntegerField(default=0)
    janak = models.PositiveIntegerField(default=0)
    kdpangkat = models.CharField(max_length=2, blank=True, null=True)
    kdeselon = models.CharField(max_length=2, blank=True, null=True)
    gapok = models.PositiveIntegerField(default=0)
    tjistri = models.PositiveIntegerField(default=0)
    tjanak = models.PositiveIntegerField(default=0)
    tjeselon = models.PositiveIntegerField(default=0)
    tjfungsi = models.PositiveIntegerField(default=0)
    tjstruk = models.PositiveIntegerField(default=0)
    # tjkhusus = models.PositiveIntegerField(default=0)
    # tbulat = models.PositiveIntegerField(default=0)
    tjumum = models.PositiveIntegerField(default=0)
    tunjangan_sertifikasi = models.PositiveIntegerField(default=0)
    tunjangan_jasa_medis = models.PositiveIntegerField(default=0)
    tunjangan_penghasilan_pegawai = models.PositiveIntegerField(default=0)
    status_pegawai = models.CharField(max_length=50, choices=CHOICES_STATUS_PEGAWAI, default='Aktif')
    history = HistoricalRecords()

    def __str__(self):
        return "{} - {} - {} - {}".format(self.id, self.nip, self.nama, self.nmskpd)

    @cached_property
    def THP(self):
        return self.gaji_pokok + self.tunjangan_istri + self.tunjangan_anak + self.tunjangan_eselon + \
               self.tunjangan_fungsional + self.tunjangan_struktural + self.tunjangan_umum + \
               self.tunjangan_sertifikasi + self.tunjangan_jasa_medis + self.tunjangan_penghasilan_pegawai

    # def DPI(self):
    #     if self.THP > 12000000:
    #         return 12000000
    #     else:
    #         return self.THP

    # def iuran1(self):
    #     return 0.01 * self.DPI()

    # def iuran4(self):
    #     return 0.04 * self.DPI()

    # def iuran5(self):
    #     return self.iuran1() + self.iuran4()

    # def gaji_induk(self):
    #     return self.gaji_pokok + self.tunjangan_istri + self.tunjangan_anak + self.tunjangan_eselon
    #     + self.tunjangan_fungsional + self.tunjangan_struktural + self.tunjangan_umum

    # def sisaiuran1(self):
    #     return self.gaji_induk - self.iuran1

    # def sisaiuran4(self):
    #     return self.gaji_induk - self.iuran4

    # def sisaiuran5(self):
    #     return self.sisaiuran1 + self.sisaiuran4
