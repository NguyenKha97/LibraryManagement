from django.shortcuts import render
from .models import DocGia


# Create your views here.
def quan_ly_doc_gia_view(request):
    if request.method == 'POST':
        button = request.POST.get('button')
        if button == 'them':
            # Lấy dữ liệu từ form
            ma_doc_gia = request.POST.get('ma-doc-gia')
            ten_doc_gia = request.POST.get('ten-doc-gia')
            ngay_sinh = request.POST.get('ngay-sinh')
            so_dien_thoai = request.POST.get('so-dien-thoai')
            ngay_tao_the = request.POST.get('ngay-tao-the')
            ngay_het_han = request.POST.get('ngay-het-han')
            dia_chi = request.POST.get('dia-chi')
            # Thêm dữ liệu vào database (bảng DocGia)
            doc_gia = DocGia(ma_doc_gia=ma_doc_gia,
                             ten_doc_gia=ten_doc_gia,
                             ngay_sinh=ngay_sinh,
                             so_dien_thoai=so_dien_thoai,
                             ngay_tao_the=ngay_tao_the,
                             ngay_het_han=ngay_het_han,
                             dia_chi=dia_chi)
            doc_gia.save()

            # Trả về thông báo khi thêm thành công (tùy chỉnh theo ý của bạn)
            print("Đã thêm dữ liệu vào database thành công!")
    data = DocGia.objects.all()  # Hoặc bạn có thể thêm điều kiện lọc dữ liệu cụ thể tại đây
    context = {
        'new_data': data,
    }
    return render(request, 'quanLyDocGia.html', context)
