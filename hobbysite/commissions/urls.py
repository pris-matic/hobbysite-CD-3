from django.urls import path
from .views import commissions_list, commission_detail

urlpatterns = [
    path('/commissions/list', commissions_list, name='commissions_list'),
    path('/commissions/detail/1', commission_detail, name='commission_detail'),
]

app_name = "commissions"