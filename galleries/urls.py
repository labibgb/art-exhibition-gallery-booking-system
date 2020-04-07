from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='galleries'),
    path('<int:gallery_id>', views.gallery, name='gallery')
]