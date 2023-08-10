from django.urls import path
from . import views

urlpatterns = [
    path('', views.quan_ly_sach_view, name='quan_ly_sach'),
]
