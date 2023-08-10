from django.urls import path
from . import views

urlpatterns = [
    path('', views.quan_ly_doc_gia_view, name='quan_ly_doc_gia'),

    path('update/', views.update_doc_gia, name='update_dg'),
    path('add/', views.add_doc_gia, name='add_dg'),
    path('delete/', views.delete_doc_gia, name='delete_dg'),
    path('search/', views.search_doc_gia, name='search_dg'),
]
