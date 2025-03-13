from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('merchstore/', include('merchstore.urls')),
    path('admin/', admin.site.urls),
]