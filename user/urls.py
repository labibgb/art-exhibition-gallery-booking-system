from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Login , name='login'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout')
]