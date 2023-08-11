from django.shortcuts import render, get_object_or_404, redirect
from .models import Sach
from .modules.inputForm import AddBook, UpdateBook
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.


def quan_ly_sach_view(request):
	button = request.POST.get('button')
	if button == 'back':
		return redirect('menu')
	books = Sach.objects.all()
	addForm = AddBook()
	updateForm = UpdateBook()

	context = {
		'books': books,
		'addForm': addForm,
		'updateForm': updateForm,
	}
	button = request.POST.get('button')
	if button == 'back':
		return redirect('menu')

	return render(request, 'quanLySach.html', context)

def update_sach(request):
	if request.method == 'POST':
		ma_sach = request.POST.get('ma_sach')
		sach = get_object_or_404(Sach, ma_sach=ma_sach)
		updateForm = UpdateBook(request.POST, instance=sach)
		try:
			if updateForm.is_valid():
				updateForm.save()
			else:
				print(updateForm.errors)
		except not sach:
			return HttpResponse("Sách không tồn tại")
	return redirect('quan_ly_sach')

def add_sach(request):
	if request.method == 'POST':
		addForm = AddBook(request.POST)
		if addForm.is_valid():
			addForm.save()
		else:
			print(addForm.errors)
	return redirect('quan_ly_sach')

def delete_sach(request):
	if request.method == 'POST':
		ma_sach = request.POST.get('ma_sach')
		sach = Sach.objects.get(ma_sach=ma_sach)
		print("delete::: " + str(sach))
		sach.delete()

	return redirect('quan_ly_sach')

def search_sach(request):
	addForm = AddBook()
	updateForm = UpdateBook()
	search_params = {
		'ma_sach': request.GET.get('ma-sach'),
		'ten_sach': request.GET.get('ten-sach'),
		'loai_sach': request.GET.get('loai-sach'),
		'ten_tac_gia': request.GET.get('tac-gia'),
		'nam_xuat_ban': request.GET.get('nam-xuat-ban'),
	}

	q_objects = Q()

	for field, value in search_params.items():
		if value:
			q_objects &= Q(**{field: value})

	matched_books = Sach.objects.filter(q_objects)
	print(q_objects)
	context = {
		'books': matched_books,
		'addForm': addForm,
		'updateForm': updateForm
	}
	return render(request, 'quanLySach.html', context)
