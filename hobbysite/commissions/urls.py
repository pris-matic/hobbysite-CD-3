from django.urls import path
from .views import commissions_list, commission_detail

urlpatterns = [
    path('list', commissions_list, name='commissions_list'),
    path('detail/<int:pk>', commission_detail, name='commission_detail'),
]

app_name = "commissions"