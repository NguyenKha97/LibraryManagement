from django.urls import path
from . import views

urlpatterns = [
    path('quan_ly_doc_gia/', views.quan_ly_doc_gia_view, name='quan_ly_doc_gia'),
]