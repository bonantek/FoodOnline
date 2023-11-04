from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.markeplace, name='marketplace'),
    path('<slug:vendor_slug>/', views.vendor_detail, name='vendor_detail'),


]