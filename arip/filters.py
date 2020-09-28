import django_filters
from .models import DataPegawai, BayarTagihan, Rekonsiliasi


class DataPegawaiFilter(django_filters.FilterSet):
    tglgaji_month = django_filters.NumberFilter(field_name='tglgaji', lookup_expr='month')
    tglgaji_year = django_filters.NumberFilter(field_name='tglgaji', lookup_expr='year')

    class Meta:
        model = DataPegawai
        fields = ['tglgaji',
                  'pemda',
                  'nmskpd',
                  ]


class BayarTagihanFilter(django_filters.FilterSet):
    bulan_tagihan_month = django_filters.NumberFilter(field_name='bulan_tagihan', lookup_expr='month')
    bulan_tagihan_year = django_filters.NumberFilter(field_name='bulan_tagihan', lookup_expr='year')

    class Meta:
        model = BayarTagihan
        fields = ['bulan_tagihan',
                  ]


class RekonsiliasiFilter(django_filters.FilterSet):
    bulan_tagihan_month = django_filters.NumberFilter(field_name='bulan_tagihan', lookup_expr='month')
    bulan_tagihan_year = django_filters.NumberFilter(field_name='bulan_tagihan', lookup_expr='year')

    class Meta:
        model = Rekonsiliasi
        fields = ['bulan_tagihan',
                  ]
