from django.urls import path
from . import views

urlpatterns = [
    path('', views.quan_ly_sach_view, name='quan_ly_sach'),
    path('update/', views.update_sach, name='update_sach'),
    path('add/', views.add_sach, name='add_sach'),
    path('delete/', views.delete_sach, name='delete_sach'),
    path('search/', views.search_sach, name='search_sach'),
]
