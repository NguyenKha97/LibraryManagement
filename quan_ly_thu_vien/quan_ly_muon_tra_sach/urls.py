from django.urls import path
from . import views

urlpatterns = [
    path('muon-sach/', views.quan_ly_muon_sach_view, name='quan_ly_muon_sach'),
    path('tra-sach', views.quan_ly_tra_sach_view, name='quan_ly_tra_sach'),
    path('tt-muon-tra/', views.thong_tin_muon_tra_view, name='thong_tin_muon_tra')

]
