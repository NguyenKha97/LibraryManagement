from django import forms
from ..models import Sach

class AddBook(forms.ModelForm):
    class Meta:
        model = Sach
        fields = ['ma_sach', 'ten_sach', 'ten_tac_gia', 'loai_sach', 'nam_xuat_ban', 'so_luong']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'author': forms.TextInput(attrs={'class': 'form-control'}),
        #     'publication_date': forms.DateInput(attrs={'class': 'form-control'}),
        # }
        labels = {
            'ma_sach': 'Mã sách:',
            'ten_sach': 'Tên sách:',
            'ten_tac_gia': 'Tên tác giả:',
            'loai_sach': 'Loại sách:',
            'nam_xuat_ban': 'Năm xuất bản:',
            'so_luong': 'Số lượng:',
        }

class UpdateBook(forms.ModelForm):
    class Meta:
        model = Sach
        fields = ['ma_sach', 'ten_sach', 'ten_tac_gia', 'loai_sach', 'nam_xuat_ban', 'so_luong']
        widgets = {
            'ma_sach': forms.TextInput(attrs={'id': 'ma_sach', 'readonly': 'readonly'}),
            'ten_sach': forms.TextInput(attrs={'id': 'ten_sach'}),
            'ten_tac_gia': forms.TextInput(attrs={'id': 'ten_tac_gia'}),
            'loai_sach': forms.Select(attrs={'id': 'loai_sach'}),
            'nam_xuat_ban': forms.DateTimeInput(attrs={'id': 'nam_xuat_ban'}),
            'so_luong': forms.NumberInput(attrs={'id': 'so_luong'})
        }
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['ma_sach'].widget.attrs.update({'id': 'ma_sach', 'disabled': 'disabled'})
        #     self.fields['ten_sach'].widget.attrs.update({'id': 'ten_sach'})
        #     self.fields['ten_tac_gia'].widget.attrs.update({'id': 'ten_tac_gia'})
        #     self.fields['loai_sach'].widget.attrs.update({'id': 'loai_sach'})
        #     self.fields['nam_xuat_ban'].widget.attrs.update({'id': 'nam_xuat_ban'})
        #     self.fields['so_luong'].widget.attrs.update({'id': 'so_luong'})

        labels = {
            'ma_sach': 'Mã sách',
            'ten_sach': 'Tên sách:',
            'ten_tac_gia': 'Tên tác giả:',
            'loai_sach': 'Loại sách:',
            'nam_xuat_ban': 'Năm xuất bản:',
            'so_luong': 'Số lượng:',
        }

