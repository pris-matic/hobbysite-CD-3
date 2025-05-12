from django.urls import path
from .views import update_profile, register, password_reset

urlpatterns = [
    path('profile/',update_profile, name='update_profile'),
    path('register/',register, name='register'),
    path('reset/', password_reset, name='password_reset'),
]

app_name = 'user_management'
