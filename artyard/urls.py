from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include( 'pages.urls')),
    path('galleries/', include( 'galleries.urls')),
    path('user/', include( 'user.urls')),
    path('booking/', include( 'booking.urls')),
    path('payment/', include( 'payment.urls')),
    path('blog/', include( 'blog.urls')),
     path('feedback/', include( 'feedback.urls')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
