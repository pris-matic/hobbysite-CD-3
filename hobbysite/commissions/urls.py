from django.urls import path
from .views import commissions_list, commission_detail, commission_create_view

urlpatterns = [
    path('list/', commissions_list, name='commissions_list'),
    path('detail/<int:id>/', commission_detail, name='commission_detail'),
    path('add/', commission_create_view, name='commission_create'),
]

app_name = "commissions"
