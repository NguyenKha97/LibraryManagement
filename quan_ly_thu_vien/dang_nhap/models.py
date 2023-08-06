from django.db import models
# Create your models here.


class Thuthu(models.Model):
    ma_thu_thu = models.CharField(max_length=10, unique=True)
    ten_thu_thu = models.CharField(max_length=50)
    mat_khau = models.CharField(max_length=30)  # Lưu mật khẩu đã được hash

    def __str__(self):
        return f'[{self.ma_thu_thu}, {self.ten_thu_thu}, {self.mat_khau}]'

