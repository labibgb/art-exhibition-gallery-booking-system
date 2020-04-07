from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include( 'pages.urls')),
    path('galleries/', include( 'galleries.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, documect_root=settings.MEDIA_ROOT )
