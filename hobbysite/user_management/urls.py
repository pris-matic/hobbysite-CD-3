from django.urls import path
from .views import update_profile, homepage

urlpatterns = [
    path('profile/',update_profile, name='update_profile'),
    path('home/',homepage ,name='home'),
]

app_name = 'user_management'