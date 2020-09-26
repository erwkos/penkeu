from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import DataPegawai, BayarTagihan, Rekonsiliasi
from django.contrib.auth.decorators import login_required
# from .filters import DataPegawaiFilter, BayarTagihanFilter, RekonsiliasiFilter
from .forms import UpdatePegawaiForm, UploadBuktiBayarForm, RekonsiliasiForm
from django.db.models import Sum
from penkeu.decorators import duta_only, allowed_users


@login_required(login_url="/login")
def datapegawai(request):
    bulan_month = request.GET.get('bulan_month')
    bulan_year = request.GET.get('bulan_year')
    queryset = DataPegawai.objects.filter(user=request.user, bulan__month=bulan_month, bulan__year=bulan_year,
                                          status_pegawai='Aktif')

    # filter
    myFilter = DataPegawaiFilter(request.GET, queryset=queryset)
    queryset = myFilter.qs

    context = {'queryset': queryset}
    return render(request, 'arip/datapegawai.html', context)


@login_required(login_url="/login")
def updatepegawai(request, id):
    datapegawai = get_object_or_404(DataPegawai, id=id)
    form = UpdatePegawaiForm(request.POST or None, instance=datapegawai)
    if form.is_valid():
        form.save()
        return redirect('/datapegawai')
    context = {'form': form,
               'datapegawai': datapegawai,
               }
    return render(request, 'arip/updatepegawai.html', context)


@login_required(login_url="/login")
def dashboardSKPD(request):
    bulan_month = request.GET.get('bulan_month')
    bulan_year = request.GET.get('bulan_year')
    queryset = DataPegawai.objects.filter(user=request.user, bulan__month=bulan_month, bulan__year=bulan_year,
                                          status_pegawai='Aktif')

    # filter
    myFilter = DataPegawaiFilter(request.GET, queryset=queryset)
    queryset = myFilter.qs

    # dashboard counts
    jumlah_pegawai = queryset.count()
    jumlah_suami_istri = queryset.aggregate(Sum('jumlah_suami_istri'))['jumlah_suami_istri__sum'] or 0
    jumlah_anak = queryset.aggregate(Sum('jumlah_anak'))['jumlah_anak__sum'] or 0
    jumlah_tanggungan = jumlah_suami_istri + jumlah_anak
    gaji_pokok = queryset.aggregate(Sum('gaji_pokok'))['gaji_pokok__sum'] or 0
    tunjangan_istri = queryset.aggregate(Sum('tunjangan_istri'))['tunjangan_istri__sum'] or 0
    tunjangan_anak = queryset.aggregate(Sum('tunjangan_anak'))['tunjangan_anak__sum'] or 0
    tunjangan_eselon = queryset.aggregate(Sum('tunjangan_eselon'))['tunjangan_eselon__sum'] or 0
    tunjangan_fungsional = queryset.aggregate(Sum('tunjangan_fungsional'))['tunjangan_fungsional__sum'] or 0
    tunjangan_struktural = queryset.aggregate(Sum('tunjangan_struktural'))['tunjangan_struktural__sum'] or 0
    tunjangan_umum = queryset.aggregate(Sum('tunjangan_umum'))['tunjangan_umum__sum'] or 0
    tunjangan_sertifikasi = queryset.aggregate(Sum('tunjangan_sertifikasi'))['tunjangan_sertifikasi__sum'] or 0
    tunjangan_jasa_medis = queryset.aggregate(Sum('tunjangan_jasa_medis'))['tunjangan_jasa_medis__sum'] or 0
    tunjangan_penghasilan_pegawai = queryset.aggregate(Sum('tunjangan_penghasilan_pegawai'))[
                                        'tunjangan_penghasilan_pegawai__sum'] or 0

    context = {'jumlah_pegawai': jumlah_pegawai,
               'jumlah_tanggungan': jumlah_tanggungan,
               'gaji_pokok': gaji_pokok,
               'tunjangan_istri': tunjangan_istri,
               'tunjangan_anak': tunjangan_anak,
               'tunjangan_eselon': tunjangan_eselon,
               'tunjangan_fungsional': tunjangan_fungsional,
               'tunjangan_struktural': tunjangan_struktural,
               'tunjangan_umum': tunjangan_umum,
               'tunjangan_sertifikasi': tunjangan_sertifikasi,
               'tunjangan_jasa_medis': tunjangan_jasa_medis,
               'tunjangan_penghasilan_pegawai': tunjangan_penghasilan_pegawai,
               }
    return render(request, 'arip/dashboardSKPD.html', context)


@login_required(login_url="/login")
@duta_only
@allowed_users(allowed_roles=['duta'])
def dashboardduta(request):
    bulan_month = request.GET.get('bulan_month')
    bulan_year = request.GET.get('bulan_year')
    queryset = DataPegawai.objects.filter(bulan__month=bulan_month, bulan__year=bulan_year, status_pegawai='Aktif')

    # filter
    myFilter = DataPegawaiFilter(request.GET, queryset=queryset)
    queryset = myFilter.qs

    # dashboard counts
    jumlah_pegawai = queryset.count()
    jumlah_suami_istri = queryset.aggregate(Sum('jumlah_suami_istri'))['jumlah_suami_istri__sum'] or 0
    jumlah_anak = queryset.aggregate(Sum('jumlah_anak'))['jumlah_anak__sum'] or 0
    jumlah_tanggungan = jumlah_suami_istri + jumlah_anak
    gaji_pokok = queryset.aggregate(Sum('gaji_pokok'))['gaji_pokok__sum'] or 0
    tunjangan_istri = queryset.aggregate(Sum('tunjangan_istri'))['tunjangan_istri__sum'] or 0
    tunjangan_anak = queryset.aggregate(Sum('tunjangan_anak'))['tunjangan_anak__sum'] or 0
    tunjangan_eselon = queryset.aggregate(Sum('tunjangan_eselon'))['tunjangan_eselon__sum'] or 0
    tunjangan_fungsional = queryset.aggregate(Sum('tunjangan_fungsional'))['tunjangan_fungsional__sum'] or 0
    tunjangan_struktural = queryset.aggregate(Sum('tunjangan_struktural'))['tunjangan_struktural__sum'] or 0
    tunjangan_umum = queryset.aggregate(Sum('tunjangan_umum'))['tunjangan_umum__sum'] or 0
    tunjangan_sertifikasi = queryset.aggregate(Sum('tunjangan_sertifikasi'))['tunjangan_sertifikasi__sum'] or 0
    tunjangan_jasa_medis = queryset.aggregate(Sum('tunjangan_jasa_medis'))['tunjangan_jasa_medis__sum'] or 0
    tunjangan_penghasilan_pegawai = queryset.aggregate(Sum('tunjangan_penghasilan_pegawai'))[
                                        'tunjangan_penghasilan_pegawai__sum'] or 0
    total_THP = gaji_pokok + tunjangan_istri + tunjangan_anak + tunjangan_eselon + tunjangan_fungsional + \
                tunjangan_struktural + tunjangan_umum + tunjangan_sertifikasi + tunjangan_jasa_medis + \
                tunjangan_penghasilan_pegawai
    total_DPI = 0
    iuran1 = 0
    iuran4 = 0
    iuran5 = 0
    for queryset in queryset:
        total_DPI = total_DPI + queryset.DPI()
        iuran1 = iuran1 + queryset.iuran1()
        iuran4 = iuran4 + queryset.iuran4()
        iuran5 = iuran5 + queryset.iuran5()

    context = {'jumlah_pegawai': jumlah_pegawai,
               'jumlah_tanggungan': jumlah_tanggungan,
               'total_THP': total_THP,
               'total_DPI': total_DPI,
               'myFilter': myFilter,
               'iuran1': iuran1,
               'iuran4': iuran4,
               'iuran5': iuran5,
               }
    return render(request, 'arip/dashboardduta.html', context)


@login_required(login_url="/login")
@allowed_users(allowed_roles=['duta'])
def history(request):
    bulan_month = request.GET.get('bulan_month')
    bulan_year = request.GET.get('bulan_year')
    queryset = DataPegawai.objects.filter(bulan__month=bulan_month, bulan__year=bulan_year)

    # filter
    myFilter = DataPegawaiFilter(request.GET, queryset=queryset)
    queryset = myFilter.qs

    for data in queryset:
        queryset = data.history.filter(history_type='~').order_by('history_date')
    context = {'queryset': queryset}
    return render(request, 'arip/history.html', context)


@login_required(login_url="/login")
@allowed_users(allowed_roles=['duta'])
def uploadbuktibayar(request):
    if request.method == 'POST':
        form = UploadBuktiBayarForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/laporan/buktibayar/')
    else:
        form = UploadBuktiBayarForm()
    context = {'form': form}
    return render(request, 'arip/uploadbuktibayar.html', context)


@login_required(login_url="/login")
@allowed_users(allowed_roles=['duta'])
def laporanbuktibayar(request):
    bulan_tagihan_month = request.GET.get('bulan_tagihan_month')
    bulan_tagihan_year = request.GET.get('bulan_tagihan_year')
    queryset = BayarTagihan.objects.filter(bulan_tagihan__month=bulan_tagihan_month,
                                           bulan_tagihan__year=bulan_tagihan_year)

    # filter
    myFilter = BayarTagihanFilter(request.GET, queryset=queryset)
    queryset = myFilter.qs

    context = {'queryset': queryset}
    return render(request, 'arip/laporanbuktibayar.html', context)


@login_required(login_url="/login")
@allowed_users(allowed_roles=['duta'])
def uploadbarekonsiliasi(request):
    if request.method == 'POST':
        form = RekonsiliasiForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/laporan/ba/rekonsiliasi/')
    else:
        form = RekonsiliasiForm()
    context = {'form': form}
    return render(request, 'arip/uploadbarekonsiliasi.html', context)


@login_required(login_url="/login")
@allowed_users(allowed_roles=['duta'])
def laporanbarekonsiliasi(request):
    bulan_tagihan_month = request.GET.get('bulan_tagihan_month')
    bulan_tagihan_year = request.GET.get('bulan_tagihan_year')
    queryset = Rekonsiliasi.objects.filter(bulan_tagihan__month=bulan_tagihan_month,
                                           bulan_tagihan__year=bulan_tagihan_year)

    # filter
    myFilter = RekonsiliasiFilter(request.GET, queryset=queryset)
    queryset = myFilter.qs

    context = {'queryset': queryset}
    return render(request, 'arip/laporanbarekonsiliasi.html', context)
