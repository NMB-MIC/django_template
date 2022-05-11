from django import forms

from app_spareparts.models import Sparepart

class SparepartModelForm(forms.ModelForm):
    #accepted = forms.BooleanField(required=True,label='ข้อความยาวๆๆ')
    class Meta:
        model = Sparepart
        fields = ['name','part_number','sub_group','qty','maker','image']
        labels = {
            'name': 'รายชื่ออุปกรณ์',
            'part_number': 'รหัสอุปกรณ์',
        }

class RestockModelForm(forms.ModelForm):
    #accepted = forms.BooleanField(required=True,label='ข้อความยาวๆๆ')
    class Meta:
        model = Sparepart
        fields = ['qty']
        labels = {
            'qty': 'เพิ่มจำนวน',
        }




