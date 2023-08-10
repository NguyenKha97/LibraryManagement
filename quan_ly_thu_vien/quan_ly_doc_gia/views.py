from django.shortcuts import render, get_object_or_404, redirect
from .models import DocGia
from .modules.inputforms import AddDocGia, UpdateDocGia
from django.http import HttpResponse
from django.db.models import Q



# Create your views here.
def quan_ly_doc_gia_view(request):

	readers = DocGia.objects.all()
	addForm = AddDocGia()
	updateForm = UpdateDocGia()

	context = {
		'readers': readers,
		'addForm': addForm,
		'updateForm': updateForm,
	}
	return render(request, 'quanLyDocGia.html', context)

def add_doc_gia(request):
	if request.method == 'POST':
		addForm = AddDocGia(request.POST)
		if addForm.is_valid():
			addForm.save()  # Lưu dữ liệu vào database
		else:
			print(addForm.errors)
	return redirect('quan_ly_doc_gia')

def update_doc_gia(request):
	if request.method == 'POST':
		ma = request.POST.get('ma_doc_gia')
		dg = get_object_or_404(DocGia, ma_doc_gia=ma)
		updateForm = UpdateDocGia(request.POST, instance=dg)
		try:
			if updateForm.is_valid():
				updateForm.save()
			else:
				print(updateForm.errors)
		except not dg:
			return HttpResponse("Độc giả không tồn tại")
	return redirect('quan_ly_doc_gia')

def delete_doc_gia(request):
	if request.method == 'POST':
		ma = request.POST.get('ma_doc_gia')
		dg = DocGia.objects.get(ma_doc_gia=ma)
		print("delete::: " + str(dg))
		dg.delete()

	return redirect('quan_ly_doc_gia')

def search_doc_gia(request):
	addForm = AddDocGia()
	updateForm = UpdateDocGia()
	search_params = {
		'ma_doc_gia': request.GET.get('ma-doc-gia'),
		'ten_doc_gia': request.GET.get('ten-doc-gia'),
		'so_dien_thoai': request.GET.get('so-dien-thoai'),
	}

	q_objects = Q()

	for field, value in search_params.items():
		if value:
			q_objects &= Q(**{field: value})

	matched_readers = DocGia.objects.filter(q_objects)
	print(q_objects)
	context = {
		'readers': matched_readers,
		'addForm': addForm,
		'updateForm': updateForm
	}
	return render(request, 'quanLyDocGia.html', context)
