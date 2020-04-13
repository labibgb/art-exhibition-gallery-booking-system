from django.urls import path
from . import views
urlpatterns = [
    path('', views.payment, name='payment'),
    path('pay', views.makePayment, name='pay'),
]