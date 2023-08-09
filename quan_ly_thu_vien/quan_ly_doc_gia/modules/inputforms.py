from django import forms
from ..models import DocGia

class AddDocGia(forms.ModelForm):
    class Meta:
        model = DocGia
        fields = ['ma_doc_gia', 'ten_doc_gia', 'ngay_sinh', 'so_dien_thoai', 'ngay_tao_the', 'ngay_het_han', 'dia_chi']
        widgets = {
            'ngay_sinh': forms.DateInput(attrs={'id': 'ngay_sinh', 'type': 'date'}),
            'ngay_tao_the': forms.DateInput(attrs={'id': 'ngay_tao_the', 'type': 'date'}),
            'ngay_het_han': forms.DateInput(attrs={'id': 'ngay_het_han', 'type': 'date'}),
        }
        labels = {
            'ma_doc_gia': 'Mã độc giả:',
            'ten_doc_gia': 'Tên độc giả:',
            'ngay_sinh': 'Ngày sinh:',
            'so_dien_thoai': 'Số điện thoại:',
            'ngay_tao_the': 'Ngày tạo thẻ:',
            'ngay_het_han': 'Ngày hết hạn:',
            'dia_chi': 'Địa chỉ:',
        }

class UpdateDocGia(forms.ModelForm):
    class Meta:
        model = DocGia
        fields = ['ma_doc_gia', 'ten_doc_gia', 'ngay_sinh', 'so_dien_thoai', 'ngay_tao_the', 'ngay_het_han', 'dia_chi']
        widgets = {
            'ma_doc_gia': forms.TextInput(attrs={'id': 'ma_doc_gia', 'readonly': 'readonly'}),
            'ten_doc_gia': forms.TextInput(attrs={'id': 'ten_doc_gia'}),
            'ngay_sinh': forms.DateInput(attrs={'id': 'ngay_sinh', 'type': 'date'}),
            'so_dien_thoai': forms.TextInput(attrs={'id': 'so_dien_thoai'}),
            'ngay_tao_the': forms.DateInput(attrs={'id': 'ngay_tao_the', 'type': 'date'}),
            'ngay_het_han': forms.DateInput(attrs={'id': 'ngay_het_han', 'type': 'date'}),
            'dia_chi': forms.Textarea(attrs={'id': 'dia_chi'})
        }

        labels = {
            'ma_doc_gia': 'Mã độc giả:',
            'ten_doc_gia': 'Tên độc giả:',
            'ngay_sinh': 'Ngày sinh:',
            'so_dien_thoai': 'Số điện thoại:',
            'ngay_tao_the': 'Ngày tạo thẻ:',
            'ngay_het_han': 'Ngày hết hạn:',
            'dia_chi': 'Địa chỉ:',
        }

