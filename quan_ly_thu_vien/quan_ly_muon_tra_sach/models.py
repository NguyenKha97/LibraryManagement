from django.db import models
from django.apps import apps

from dang_nhap.models import Thuthu
from quan_ly_doc_gia.models import DocGia
from quan_ly_sach.models import Sach


# Create your models here.

class MuonTraSach(models.Model):
    ma_thu_thu = models.ForeignKey(Thuthu, on_delete=models.CASCADE, default='')
    ma_doc_gia = models.ForeignKey(DocGia, on_delete=models.CASCADE, default='')
    ma_sach = models.ForeignKey(Sach, on_delete=models.CASCADE, default='')
    so_luong = models.IntegerField()
    ngay_muon = models.DateField()
    ngay_hen_tra = models.DateField()
    ngay_tra = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ('ma_thu_thu', 'ma_doc_gia', 'ma_sach', 'ngay_muon')

    def __str__(self):
        return f"[{self.ma_thu_thu} - {self.ma_doc_gia} - {self.ma_sach} - {self.so_luong} - {self.ngay_muon} - {self.ngay_hen_tra} - {self.ngay_tra}]"
