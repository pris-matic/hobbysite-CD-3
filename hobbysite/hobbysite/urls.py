from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('merchstore/', include('merchstore.urls')),
    path('blog/', include('blog.urls')),
    path('commissions/', include('commissions.urls')),
    path('forum/', include('forum.urls')),
    path('wiki/', include('wiki.urls')),   
]
