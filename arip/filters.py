# import django_filters
# from .models import DataPegawai, BayarTagihan, Rekonsiliasi

# class DataPegawaiFilter(django_filters.FilterSet):
#     bulan_month = django_filters.NumberFilter(field_name='bulan', lookup_expr='month')
#     bulan_year = django_filters.NumberFilter(field_name='bulan', lookup_expr='year')
    
#     class Meta:
#         model = DataPegawai
#         fields = [  'bulan',
#                     'pemda',
#                     'skpd',
#                 ]
                
# class BayarTagihanFilter(django_filters.FilterSet):
#     bulan_tagihan_month = django_filters.NumberFilter(field_name='bulan_tagihan', lookup_expr='month')
#     bulan_tagihan_year = django_filters.NumberFilter(field_name='bulan_tagihan', lookup_expr='year')
    
#     class Meta:
#         model = BayarTagihan
#         fields = [  'bulan_tagihan',
#                 ]

# class RekonsiliasiFilter(django_filters.FilterSet):
#     bulan_tagihan_month = django_filters.NumberFilter(field_name='bulan_tagihan', lookup_expr='month')
#     bulan_tagihan_year = django_filters.NumberFilter(field_name='bulan_tagihan', lookup_expr='year')
    
#     class Meta:
#         model = Rekonsiliasi
#         fields = [  'bulan_tagihan',
#                 ]
                