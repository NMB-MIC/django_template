from django.contrib import admin

from app_spareparts.models import Sparepart
# Register your models here.

class SparepartAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'part_number','sub_group', 'qty', 'maker']
    search_fields = ['part_number']
    list_filter = ['qty']

admin.site.register(Sparepart, SparepartAdmin)