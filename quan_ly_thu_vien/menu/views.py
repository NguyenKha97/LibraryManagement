from django.shortcuts import render, redirect
# Create your views here.


def menu_view(request):
    if request.method == 'POST':
        button = request.POST.get('button')
        if button == 'sach':
            # Xử lý khi nhấn nút "Quản lý sách"
            return redirect('quan_ly_sach')
        elif button == 'docgia':
            # Xử lý khi nhấn nút "Quản lý độc giả"
            return redirect('quan_ly_doc_gia')
        elif button == 'muontra':
            # Xử lý khi nhấn nút "Quản lý mượn - trả"
            return redirect('quan_ly_muon_sach')
        elif button == 'dangxuat':
            request.session.clear()
            return redirect('dang_nhap')
    return render(request, 'menu.html')
