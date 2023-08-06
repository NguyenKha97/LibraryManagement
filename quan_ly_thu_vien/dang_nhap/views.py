from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Thuthu


# Create your views here.


def dang_nhap_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'Username: {username}; Password: {password}')

        try:
            # Truy vấn dữ liệu trong database
            user = Thuthu.objects.get(ma_thu_thu=username)
            # Kiểm tra mật khẩu
            if user.mat_khau == password:
                # Đăng nhập thành công, chuyển hướng đến trang menu.html
                return redirect('menu')
            else:
                # Sai mật khẩu, trả về thông báo lỗi
                return HttpResponse("Sai mật khẩu")
        except Thuthu.DoesNotExist:
            # Không tìm thấy người dùng, trả về thông báo lỗi
            return HttpResponse("Tài khoản không tồn tại")
    return render(request, 'dangNhap.html')

