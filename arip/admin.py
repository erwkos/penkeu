from django.contrib import admin
from .models import DataPegawai, BayarTagihan, Rekonsiliasi
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from simple_history.admin import SimpleHistoryAdmin

@admin.register(DataPegawai)
class DataPegawaiAdmin(ImportExportModelAdmin):
    pass

@admin.register(BayarTagihan)
class BayarTagihanAdmin(ImportExportModelAdmin):
    pass

@admin.register(Rekonsiliasi)
class RekonsiliasiAdmin(ImportExportModelAdmin):
    pass


# @admin.register(SKPD)
# class SKPDAdmin(ImportExportModelAdmin):
#     pass

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'Profile'
#     fk_name = 'user'

# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )

#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)