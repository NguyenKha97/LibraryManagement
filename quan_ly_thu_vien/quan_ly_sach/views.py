from django.shortcuts import render


# Create your views here.
def quan_ly_sach_view(request):
	return render(request, 'quanLySach.html')
