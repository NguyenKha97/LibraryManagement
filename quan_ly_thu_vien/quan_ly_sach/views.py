from django.shortcuts import render
from .models import Sach
# Create your views here.


def quan_ly_sach_view(request):
    if request.method == 'POST':
        button = request.POST.get('button')
        if button == 'them':
            # Lấy dữ liệu từ form
            ma_sach = request.POST.get('ma-sach')
            ten_sach = request.POST.get('ten-sach')
            tac_gia = request.POST.get('tac-gia')
            nam_xuat_ban = request.POST.get('nam-xuat-ban')
            loai_sach = request.POST.get('loai-sach')
            so_luong = request.POST.get('so-luong')
            # Thêm dữ liệu vào database (bảng DocGia)
            sach = Sach(ma_sach=ma_sach,
                        ten_sach=ten_sach,
                        tac_gia=tac_gia,
                        nam_xuat_ban=nam_xuat_ban,
                        loai_sach=loai_sach,
                        so_luong=so_luong)
            sach.save()

            # Trả về thông báo khi thêm thành công (tùy chỉnh theo ý của bạn)
            print("Đã thêm dữ liệu sách vào database thành công!")
    data = Sach.objects.all()  # Hoặc bạn có thể thêm điều kiện lọc dữ liệu cụ thể tại đây
    context = {
        'new_data': data,
    }
    return render(request, 'quanLySach.html', context)
