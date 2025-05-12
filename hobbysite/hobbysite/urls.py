from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('merchstore/', include('merchstore.urls')),
    path('blog/', include('blog.urls')),
    path('commissions/', include('commissions.urls')),
    path('forum/', include('forum.urls')),
    path('wiki/', include('wiki.urls')),   
    path('',include('user_management.urls')),
    path('home/', include('dashboard.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
