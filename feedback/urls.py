from django.urls import path
from . import views
urlpatterns = [
    path('', views.Feedback , name='feedback')
]