from django.urls import path
from .views import commissions_list, commission_detail, commission_create, commission_update, job_application_evaluate 

urlpatterns = [
    path('list/', commissions_list, name='commissions_list'),
    path('detail/<int:id>/', commission_detail, name='commission_detail'),
    path('add/', commission_create, name='commission_create'),
    path('<int:id>/edit/', commission_update, name='commission_update'),
    path('jobapplications/<int:id>/evaluate', job_application_evaluate, name='job_application_evaluate')
]

app_name = "commissions"
