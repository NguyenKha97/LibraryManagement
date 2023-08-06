from django.urls import path
from . import views

urlpatterns = [
    path('', views.dang_nhap_view, name='dang_nhap'),
]
