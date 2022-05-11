from django.urls import path
from . import views

urlpatterns = [
    path('',views.spareparts,name='spareparts'),
    path('deposit/<int:sparepart_id>',views.deposit,name='deposit'),
    path('withdraw/<int:sparepart_id>',views.withdraw,name='withdraw'),
    path('new_sparepart',views.new_sparepart,name='new_sparepart'),
    path('delete/<int:sparepart_id>',views.delete,name='delete'),
]