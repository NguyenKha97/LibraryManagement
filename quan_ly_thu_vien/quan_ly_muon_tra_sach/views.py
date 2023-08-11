from django.db.models import Q
from django.shortcuts import render, redirect
from quan_ly_doc_gia.models import DocGia
from quan_ly_sach.models import Sach
from dang_nhap.models import Thuthu
from .models import MuonTraSach
from datetime import date, datetime, timedelta


# Create your views here.
def xu_ly_tim_doc_gia(request, context, stored_doc_gia, stored_sach, stored_list_sach_muon,
                      ma_doc_gia_tk):
    """Xử lý khi nút tìm kiếm mã độc giả được nhấn"""
    if stored_doc_gia and ma_doc_gia_tk == stored_doc_gia['ma_doc_gia']:
        context['doc_gia'] = stored_doc_gia
    else:
        try:
            doc_gia = DocGia.objects.get(ma_doc_gia=ma_doc_gia_tk)
            print(doc_gia)  # kiểm tra xem có kiếm được độc giả không
            request.session['stored_doc_gia'] = {
                'ma_doc_gia': doc_gia.ma_doc_gia,
                'ten_doc_gia': doc_gia.ten_doc_gia,
                'ngay_sinh': doc_gia.ngay_sinh.strftime('%d-%m-%Y'),
                'so_dien_thoai': doc_gia.so_dien_thoai,
                'ngay_het_han': doc_gia.ngay_het_han.strftime('%d-%m-%Y'),
            }
            context['doc_gia'] = request.session.get('stored_doc_gia')
        except DocGia.DoesNotExist:
            print('Khong tim thay ma doc gia')
            context['doc_gia'] = {}
            context['list_sach_muon'] = {}
            request.session['stored_doc_gia'] = {}
    if stored_sach:
        context['sach'] = stored_sach
    if context['doc_gia']:
        context['list_sach_muon'] = request.session.get('stored_list_sach_muon')
        context['sl_sach_con_lai'] = request.session.get('stored_sl_sach_con_lai')
    if 'stored_list_sach_muon' in request.session:
        ma_sach_tk = request.POST.get('ma-sach')
        for sach in request.session.get('stored_list_sach_muon'):
            if sach['ma_sach'] == ma_sach_tk:
                context['sl_sach_con_lai'] = 0


def tim_so_luong_unavailable(sachs):
    sl_sach_dang_muon = 0
    for sach in sachs:
        sl_sach_dang_muon += sach['so_luong']
    return sl_sach_dang_muon


def xu_ly_tim_sach(request, context, stored_doc_gia, stored_sach, stored_list_sach_muon,
                   ma_sach_tk):
    """Xử lý khi nút tìm kiếm mã sách được nhấn"""
    if stored_sach and ma_sach_tk == stored_sach['ma_sach']:
        context['sach'] = stored_sach
    else:
        try:
            sach = Sach.objects.get(ma_sach=ma_sach_tk)
            print(sach)  # kiểm tra co kiếm dc sách không
            request.session['stored_sach'] = {
                'ma_sach': sach.ma_sach,
                'ten_sach': sach.ten_sach,
                'the_loai': sach.loai_sach,
                'so_luong_con': sach.so_luong_con,
                'ten_tac_gia': sach.ten_tac_gia,
                'nam_xuat_ban': sach.nam_xuat_ban
            }
            context['sach'] = request.session.get('stored_sach')
            request.session['stored_sl_sach_con_lai'] = request.session.get('stored_sach')['so_luong_con']
            # context['sl_sach_con_lai'] = request.session.get('stored_sl_sach_con_lai')
        except Sach.DoesNotExist:
            print('Khong tim thay sach')
            context['sach'] = {}
            request.session['stored_sach'] = {}
        if 'stored_list_sach_muon' in request.session:
            for sach in request.session.get('stored_list_sach_muon'):
                if sach['ma_sach'] == ma_sach_tk:
                    context['sl_sach_con_lai'] = 0
                    context['sach']['so_luong_con'] -= sach['so_luong_muon']
    if stored_doc_gia:
        context['doc_gia'] = stored_doc_gia
        context['list_sach_muon'] = stored_list_sach_muon
    if context['sach']:
        context['sl_sach_con_lai'] = request.session.get('stored_sl_sach_con_lai')
    if 'stored_list_sach_muon' in request.session:
        for sach in request.session.get('stored_list_sach_muon'):
            if sach['ma_sach'] == ma_sach_tk:
                context['sl_sach_con_lai'] = 0


def quan_ly_muon_sach_view(request):
    """Xử lý logic trang mượn sách"""
    # khởi tạo biến lấy giá trị dc lưu trong session nếu có
    context = {}
    stored_doc_gia = request.session.get('stored_doc_gia')
    stored_sach = request.session.get('stored_sach')
    stored_list_sach_muon = request.session.get('stored_list_sach_muon', [])

    if request.method == 'POST':
        button = request.POST.get('button')

        if button == 'tim-doc-gia':
            ma_doc_gia_tk = request.POST.get('ma-doc-gia')
            print(button, ma_doc_gia_tk)  # kiểm tra nút dc nhấn và giá trị cua input
            xu_ly_tim_doc_gia(request, context, stored_doc_gia, stored_sach, stored_list_sach_muon,
                              ma_doc_gia_tk)
        elif button == 'tim-sach':
            ma_sach_tk = request.POST.get('ma-sach')
            print(button, ma_sach_tk)  # kiểm tra nút dc nhấn và giá trị cua input
            xu_ly_tim_sach(request, context, stored_doc_gia, stored_sach, stored_list_sach_muon,
                           ma_sach_tk)
        elif button == 'them-sach-muon':
            sl_sach_muon = int(request.POST.get('sl_sach_muon'))
            sach_muon = {
                'ma_sach': stored_sach['ma_sach'],
                'ten_sach': stored_sach['ten_sach'],
                'ten_tac_gia': stored_sach['ten_tac_gia'],
                'nam_xuat_ban': stored_sach['nam_xuat_ban'],
                'so_luong_muon': sl_sach_muon
            }
            if 'stored_list_sach_muon' in request.session:
                sach_found = False
                for sach in request.session['stored_list_sach_muon']:
                    if sach['ma_sach'] == sach_muon['ma_sach']:
                        sach['so_luong_muon'] += sl_sach_muon
                        sach_found = True
                        break

                if not sach_found:
                    request.session['stored_list_sach_muon'].append(sach_muon)
            else:
                request.session['stored_list_sach_muon'] = [sach_muon]
            context['list_sach_muon'] = request.session.get('stored_list_sach_muon')
            request.session['stored_sl_sach_con_lai'] -= sach_muon['so_luong_muon']
            # print(context['sl_sach_con_lai'])
            context['sl_sach_con_lai'] = request.session['stored_sl_sach_con_lai']
            if stored_doc_gia:
                context['doc_gia'] = stored_doc_gia
            if stored_sach:
                context['sach'] = stored_sach
                context['sach']['so_luong_con'] = request.session.get('stored_sl_sach_con_lai')
        elif button == 'huy':
            if 'stored_doc_gia' in request.session:
                del request.session['stored_doc_gia']
            if 'stored_sach' in request.session:
                del request.session['stored_sach']
            if 'stored_list_sach_muon' in request.session:
                del request.session['stored_list_sach_muon']
            if 'stored_sl_sach_con_lai' in request.session:
                del request.session['stored_sl_sach_con_lai']
            stored_doc_gia = {}
            stored_sach = {}
            stored_list_sach_muon = []
            # Clear context variables as well
            context['doc_gia'] = {}
            context['sach'] = {}
            context['list_sach_muon'] = []
            context['sl_sach_con_lai'] = 0
        elif button == 'xoa':
            ma_sach_xoa = request.POST.get('ma-sach-xoa')
            sl_sach_xoa = request.POST.get('sl-sach-xoa')
            print(int(sl_sach_xoa))
            stored_list_sach_muon = request.session.get('stored_list_sach_muon', [])
            new_stored_list_sach_muon = []

            for sach in stored_list_sach_muon:
                if sach['ma_sach'] != ma_sach_xoa:
                    new_stored_list_sach_muon.append(sach)

            request.session['stored_list_sach_muon'] = new_stored_list_sach_muon
            context['list_sach_muon'] = new_stored_list_sach_muon
            context['doc_gia'] = request.session.get('stored_doc_gia')
            context['sach'] = request.session.get('stored_sach')
            if ma_sach_xoa == request.session.get('stored_sach')['ma_sach']:
                request.session['stored_sl_sach_con_lai'] += int(sl_sach_xoa)
                context['sl_sach_con_lai'] = request.session.get('stored_sl_sach_con_lai')
                context['sach']['so_luong_con'] = request.session.get('stored_sl_sach_con_lai')
        elif button == 'muon':
            if stored_doc_gia and stored_sach and stored_list_sach_muon:
                thu_thu = Thuthu.objects.get(ma_thu_thu=request.session.get('ma_thu_thu'))
                doc_gia = DocGia.objects.get(ma_doc_gia=stored_doc_gia['ma_doc_gia'])
                sach = Sach.objects.get(ma_sach=stored_sach['ma_sach'])
                print(thu_thu, doc_gia)
                ngay_muon = datetime.now().date()
                ngay_hen_tra = ngay_muon + timedelta(days=7)
            for sach_muon in stored_list_sach_muon:
                sach = Sach.objects.get(ma_sach=sach_muon['ma_sach'])
                so_luong = sach_muon['so_luong_muon']

                # Tạo đối tượng MuonTraSach và lưu vào cơ sở dữ liệu
                muon_tra = MuonTraSach(
                    ma_thu_thu=thu_thu,
                    ma_doc_gia=doc_gia,
                    ma_sach=sach,
                    so_luong=so_luong,
                    ngay_muon=ngay_muon,
                    ngay_hen_tra=ngay_hen_tra
                )
                muon_tra.save()

                # Cập nhật số lượng mượn và số lượng còn của sách
                sach.so_luong_muon += so_luong
                sach.so_luong_con -= so_luong
                sach.save()

            # Xóa các dữ liệu trong session sau khi đã thực hiện mượn
            del request.session['stored_doc_gia']
            del request.session['stored_sach']
            del request.session['stored_list_sach_muon']
            del request.session['stored_sl_sach_con_lai']

            # Cập nhật lại các biến context để hiển thị thông tin trên trang
            context['doc_gia'] = {}
            context['sach'] = {}
            context['list_sach_muon'] = []
            context['sl_sach_con_lai'] = 0
        elif button == 'back':
            return redirect('menu')
        elif button == 'ql-tra-sach':
            return redirect('quan_ly_tra_sach')
            # return render(request, 'quanLyTraSach.html')
        elif button == 'tt-muon-tra':
            return redirect('thong_tin_muon_tra')

    return render(request, 'quanLyMuonSach.html', context)


def quan_ly_tra_sach_view(request):
    """Xử lý logic trang trả sách"""
    context = {}
    if request.method == 'POST':
        button = request.POST.get('button')
        if button == 'back':
            return redirect('menu')

        elif button == 'ql-muon-sach':
            return redirect('quan_ly_muon_sach')
        elif button == 'tt-muon-tra':
            return redirect('thong_tin_muon_tra')

        elif button == 'tim-sach-muon':
            ma_sach = request.POST.get('ma-sach')
            try:
                sach = Sach.objects.get(ma_sach=ma_sach)
                data_muon_tra = MuonTraSach.objects.filter(ma_sach=sach)

                # Convert QuerySet to a list of dictionaries
                data_muon_tra_list = []
                for muon_tra in data_muon_tra:
                    if not muon_tra.ngay_tra:
                        data_muon_tra_list.append({
                            'ma_sach': muon_tra.ma_sach.ma_sach,
                            'ma_doc_gia': muon_tra.ma_doc_gia.ma_doc_gia,
                            'so_luong': muon_tra.so_luong,
                            'ngay_muon': muon_tra.ngay_muon.strftime('%d-%m-%Y'),
                            'ngay_hen_tra': muon_tra.ngay_hen_tra.strftime('%d-%m-%Y')
                        })

                # Store the list in the session
                request.session['stored_data_muon_tra'] = data_muon_tra_list
                context['data_muon_tra'] = data_muon_tra_list
            except Sach.DoesNotExist:
                print('Khong tim thay sach')
                context['data_muon_tra'] = {}
                request.session['stored_data_muon_tra'] = []
            if request.session.get('stored_doc_gia'):
                context['doc_gia'] = request.session.get('stored_doc_gia')
                context['data_doc_gia_muon_tra'] = request.session.get('stored_data_doc_gia_muon_tra')

        elif button == 'tim-doc-gia':
            ma_doc_gia = request.POST.get('ma-doc-gia')
            try:
                doc_gia = DocGia.objects.get(ma_doc_gia=ma_doc_gia)
                data_doc_gia_muon_tra = MuonTraSach.objects.filter(ma_doc_gia=doc_gia)
                # print(doc_gia)  # kiểm tra xem có kiếm được độc giả không
                # print(data_doc_gia_muon_tra)
                # Xử lý thông tin độc giả
                request.session['stored_doc_gia'] = {
                    'ma_doc_gia': doc_gia.ma_doc_gia,
                    'ten_doc_gia': doc_gia.ten_doc_gia,
                    'ngay_sinh': doc_gia.ngay_sinh.strftime('%d-%m-%Y'),
                    'so_dien_thoai': doc_gia.so_dien_thoai,
                    'ngay_het_han': doc_gia.ngay_het_han.strftime('%d-%m-%Y'),
                }
                context['doc_gia'] = request.session.get('stored_doc_gia')

                # Xử lý hiển thị sách độc giả đã mượn
                data_doc_gia_muon_tra_list = []
                for muon_tra in data_doc_gia_muon_tra:
                    if not muon_tra.ngay_tra:
                        sach = Sach.objects.get(ma_sach=muon_tra.ma_sach.ma_sach)
                        data_doc_gia_muon_tra_list.append({
                            'ma_sach': muon_tra.ma_sach.ma_sach,
                            'ten_sach': sach.ten_sach,
                            'so_luong': muon_tra.so_luong,
                            'ngay_muon': muon_tra.ngay_muon.strftime('%d-%m-%Y'),
                            'ngay_hen_tra': muon_tra.ngay_hen_tra.strftime('%d-%m-%Y')
                        })

                # Store the list in the session
                request.session['stored_data_doc_gia_muon_tra'] = data_doc_gia_muon_tra_list
                context['data_doc_gia_muon_tra'] = data_doc_gia_muon_tra_list
            except DocGia.DoesNotExist:
                print('Khong tim thay ma doc gia')
                context['doc_gia'] = {}
                request.session['stored_doc_gia'] = {}
                context['data_doc_gia_muon_tra'] = {}
                request.session['stored_data_doc_gia_muon_tra'] = {}
            if request.session.get('stored_data_muon_tra'):
                context['data_muon_tra'] = request.session.get('stored_data_muon_tra')
        elif button == 'tra':
            ma_doc_gia = request.session.get('stored_doc_gia')['ma_doc_gia']
            ma_sach = request.POST.get('ma-sach-tra')
            so_luong = request.POST.get('sl-sach-tra')
            ngay_hen_tra = request.POST.get('ngay-hen-tra')
            print(ma_doc_gia, ma_sach, so_luong, ngay_hen_tra)
            doc_gia = DocGia.objects.get(ma_doc_gia=ma_doc_gia)
            data_doc_gia_muon_tra = MuonTraSach.objects.filter(ma_doc_gia=doc_gia)
            for muon_tra in data_doc_gia_muon_tra:
                if muon_tra.ma_sach.ma_sach == ma_sach and muon_tra.ngay_hen_tra.strftime('%d-%m-%Y') == ngay_hen_tra:
                    print(muon_tra.ngay_hen_tra.strftime('%d-%m-%Y'), ngay_hen_tra)
                    muon_tra.ngay_tra = datetime.now().date()
                    muon_tra.save()

                    sach = Sach.objects.get(ma_sach=ma_sach)
                    sach.so_luong_muon -= int(so_luong)
                    sach.so_luong_con += int(so_luong)
                    sach.save()
            # new_data_doc_gia_muon_tra_list = []
            # for muon_tra in request.session.get('stored_data_doc_gia_muon_tra'):
            #     if not muon_tra.ma_sach == ma_sach:
            #         new_data_doc_gia_muon_tra_list.append(muon_tra)
            # request.session['stored_data_doc_gia_muon_tra'] = new_data_doc_gia_muon_tra_list
            # context['data_doc_gia_muon_tra'] = new_data_doc_gia_muon_tra_list
            # context['doc_gia'] = request.session.get('stored_doc_gia')
            # context['data_muon_tra'] = new_data_doc_gia_muon_tra_list
        elif button == 'huy':
            if 'stored_data_muon_tra' in request.session:
                del request.session['stored_data_muon_tra']
            if 'stored_doc_gia' in request.session:
                del request.session['stored_doc_gia']
            if 'stored_data_doc_gia_muon_tra' in request.session:
                del request.session['stored_data_doc_gia_muon_tra']

            # Clear context variables as well
            context['data_muon_tra'] = {}
            context['doc_gia'] = {}
            context['data_doc_gia_muon_tra'] = []

    return render(request, 'quanLyTraSach.html', context)


def thong_tin_muon_tra_view(request):
    context = {}
    if request.method == 'POST':
        button = request.POST.get('button')
        if button == 'back':
            return redirect('menu')

        elif button == 'ql-muon-sach':
            return redirect('quan_ly_muon_sach')
        elif button == 'ql-tra-sach':
            return redirect('quan_ly_tra_sach')

    # Lấy dữ liệu sách đang được mượn
    data_muon_sach = MuonTraSach.objects.filter(ngay_tra__isnull=True)

    # Lấy dữ liệu sách quá hạn trả
    data_qua_han = MuonTraSach.objects.filter(ngay_tra__isnull=True, ngay_hen_tra__lt=datetime.now().date())

    # Lấy dữ liệu mượn trả của ngày hôm nay
    data_muon_tra_hom_nay = MuonTraSach.objects.filter(
        Q(ngay_muon=datetime.now().date()) | Q(ngay_tra=datetime.now().date())
    )

    # Chuyển đổi dữ liệu QuerySet thành danh sách từng dict
    data_muon_sach_list = []
    data_qua_han_list = []
    data_muon_tra_hom_nay_list = []

    for muon_tra in data_muon_sach:
        data_muon_sach_list.append({
            'ma_sach': muon_tra.ma_sach.ma_sach,
            'ma_doc_gia': muon_tra.ma_doc_gia.ma_doc_gia,
            'so_luong': muon_tra.so_luong,
            'ngay_muon': muon_tra.ngay_muon.strftime('%d-%m-%Y'),
            'ngay_hen_tra': muon_tra.ngay_hen_tra.strftime('%d-%m-%Y'),
            'con_lai': (muon_tra.ngay_hen_tra - datetime.now().date()).days
        })

    for qua_han in data_qua_han:
        data_qua_han_list.append({
            'ma_sach': qua_han.ma_sach.ma_sach,
            'ma_doc_gia': qua_han.ma_doc_gia.ma_doc_gia,
            'so_luong': qua_han.so_luong,
            'ngay_muon': qua_han.ngay_muon.strftime('%d-%m-%Y'),
            'ngay_hen_tra': qua_han.ngay_hen_tra.strftime('%d-%m-%Y'),
            'qua_han': (datetime.now().date() - qua_han.ngay_hen_tra).days
        })

    for muon_tra in data_muon_tra_hom_nay:
        entry = {
            'ma_sach': muon_tra.ma_sach.ma_sach,
            'ma_doc_gia': muon_tra.ma_doc_gia.ma_doc_gia,
            'so_luong': muon_tra.so_luong,
            'ngay_muon': muon_tra.ngay_muon.strftime('%d-%m-%Y'),
        }
        if muon_tra.ngay_tra:
            entry['ngay_tra'] = muon_tra.ngay_tra.strftime('%d-%m-%Y')
        data_muon_tra_hom_nay_list.append(entry)

    # Lưu danh sách vào context để truyền cho template
    context['data_muon_sach'] = data_muon_sach_list
    context['data_qua_han'] = data_qua_han_list
    context['data_muon_tra_hom_nay'] = data_muon_tra_hom_nay_list

    return render(request, 'thongTinMuonTra.html', context)
