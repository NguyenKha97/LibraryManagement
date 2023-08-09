from django.db import models

# Create your models here.
class Sach(models.Model):
    ma_sach = models.CharField(max_length=10, unique=True)
    ten_sach = models.CharField(max_length=200)
    ten_tac_gia = models.CharField(max_length=100)
    nam_xuat_ban = models.PositiveIntegerField()
    so_luong = models.PositiveIntegerField()
    LOAI_SACH_CHOICES = [
        ('TRUYEN', 'Truyện'),
        ('KY_NANG', 'Kỹ năng'),
        ('KIEN_THUC', 'Kiến thức'),
        ('VAN_HOC', 'Văn học'),
        ('KHOA_HOC', 'Khoa học'),
        ('KHAC', 'Khác'),
    ]
    loai_sach = models.CharField(max_length=10, choices=LOAI_SACH_CHOICES)

    def __str__(self):
        return f'[{self.ma_sach}, {self.ten_sach}, {self.ten_tac_gia}, {self.nam_xuat_ban}, {self.so_luong}, {self.loai_sach}]'
