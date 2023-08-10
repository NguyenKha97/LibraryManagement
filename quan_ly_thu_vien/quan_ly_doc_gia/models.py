from django.db import models
# Create your models here.


class DocGia(models.Model):
    ma_doc_gia = models.CharField(max_length=10, unique=True)
    ten_doc_gia = models.CharField(max_length=50)
    ngay_sinh = models.DateField()
    so_dien_thoai = models.CharField(max_length=20)
    ngay_tao_the = models.DateField()
    ngay_het_han = models.DateField()
    dia_chi = models.CharField(max_length=200)

    def __str__(self):
        return f'[{self.ma_doc_gia} - {self.ten_doc_gia} - {self.ngay_het_han}]'
