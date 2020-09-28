from django.forms import ModelForm
from .models import DataPegawai, BayarTagihan, Rekonsiliasi


class UpdatePegawaiForm(ModelForm):
    class Meta:
        model = DataPegawai
        exclude = ['nama', 'nip', 'tglgaji', 'pemda', 'nmskpd', 'history']


class UploadBuktiBayarForm(ModelForm):
    class Meta:
        model = BayarTagihan
        fields = '__all__'


class RekonsiliasiForm(ModelForm):
    class Meta:
        model = Rekonsiliasi
        fields = '__all__'

# class UpdateProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['user']
