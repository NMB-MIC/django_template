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
            'sub_group': 'ประเภท',
            'qty': 'จำนวน',
            'maker' : 'ยี่ห้อ',
            'image' : 'รูปภาพ'
        }
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'part_number': forms.TextInput(attrs={'class': 'form-control'}),
        #     'sub_group': forms.TextInput(attrs={'class': 'form-control'}),
         
        #     'maker': forms.TextInput(attrs={'class': 'form-control'}),
        # }

class RestockModelForm(forms.ModelForm):
    #accepted = forms.BooleanField(required=True,label='ข้อความยาวๆๆ')
    class Meta:
        model = Sparepart
        fields = ['qty']
        labels = {
            'qty': 'เพิ่มจำนวน',
        }

