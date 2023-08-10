from django import forms
from ..models import Sach

class AddBook(forms.ModelForm):
    class Meta:
        model = Sach
        fields = ['ma_sach', 'ten_sach', 'ten_tac_gia', 'loai_sach', 'nam_xuat_ban', 'so_luong_con']

        labels = {
            'ma_sach': 'Mã sách:',
            'ten_sach': 'Tên sách:',
            'ten_tac_gia': 'Tên tác giả:',
            'loai_sach': 'Loại sách:',
            'nam_xuat_ban': 'Năm xuất bản:',
            'so_luong_con': 'Số lượng còn lại:',
        }

class UpdateBook(forms.ModelForm):
    class Meta:
        model = Sach
        fields = ['ma_sach', 'ten_sach', 'ten_tac_gia', 'loai_sach', 'nam_xuat_ban', 'so_luong_con']
        widgets = {
            'ma_sach': forms.TextInput(attrs={'id': 'ma_sach', 'readonly': 'readonly'}),
            'ten_sach': forms.TextInput(attrs={'id': 'ten_sach'}),
            'ten_tac_gia': forms.TextInput(attrs={'id': 'ten_tac_gia'}),
            'loai_sach': forms.Select(attrs={'id': 'loai_sach'}),
            'nam_xuat_ban': forms.DateTimeInput(attrs={'id': 'nam_xuat_ban'}),
            'so_luong_con': forms.NumberInput(attrs={'id': 'so_luong_con'})
        }

        labels = {
            'ma_sach': 'Mã sách',
            'ten_sach': 'Tên sách:',
            'ten_tac_gia': 'Tên tác giả:',
            'loai_sach': 'Loại sách:',
            'nam_xuat_ban': 'Năm xuất bản:',
            'so_luong_con': 'Số lượng còn lại:',
        }

