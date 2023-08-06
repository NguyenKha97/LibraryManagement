from django.shortcuts import render


# Create your views here.
def quan_ly_doc_gia_view(request):
	return render(request, 'quanLyDocGia.html')
