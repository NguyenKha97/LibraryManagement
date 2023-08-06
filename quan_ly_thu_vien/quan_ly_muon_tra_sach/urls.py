from django.urls import path
from . import views

urlpatterns = [
    path('quan_ly_muon_tra_sach/', views.quan_ly_muon_tra_sach_view, name='quan_ly_muon_tra_sach'),
]
