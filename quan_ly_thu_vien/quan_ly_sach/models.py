from django.db import models
# Create your models here.


class Sach(models.Model):
    ma_sach = models.CharField(max_length=10, unique=True)
    ten_sach = models.CharField(max_length=100)
    loai_sach = models.CharField(max_length=50)
    tac_gia = models.CharField(max_length=100)
    nam_xuat_ban = models.IntegerField()
    so_luong_muon = models.IntegerField(default=0)
    so_luong_con = models.IntegerField(default=1)


    def __str__(self):
        return f'[{self.ma_sach} - {self.ten_sach} - {self.tac_gia} - {self.loai_sach} - {self.so_luong_con}]'
