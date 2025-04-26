from django.urls import path
from .views import update_profile

urlpatterns = [
    path('',update_profile, name='update_profile'),
]

app_name = 'user_management'