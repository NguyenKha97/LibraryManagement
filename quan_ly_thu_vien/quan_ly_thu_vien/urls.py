"""
URL configuration for quan_ly_thu_vien project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dang_nhap.urls')),
    path('dang-nhap/', include('dang_nhap.urls')),
    path('menu/', include('menu.urls')),
    path('quan-ly-doc-gia/', include('quan_ly_doc_gia.urls')),
    path('quan-ly-sach/', include('quan_ly_sach.urls')),
    path('quan-ly-muon-tra-sach/', include('quan_ly_muon_tra_sach.urls')),
]
