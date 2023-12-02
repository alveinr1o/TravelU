from django.shortcuts import render, redirect
from .models import Penumpang, Reservasi, Bus, Driver, Admin
from django.utils.safestring import mark_safe
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'index.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    #SELECT * WHERE username = username, password = password
    penumpang = Penumpang.objects.filter(username = username, password = password)
    if penumpang.exists(): 
        context = {
            'penumpang': penumpang.first(),
        }
        return render(request, 'homepage.html', context)
    else :
        context = {
            'alert': mark_safe('<div class="alert"> Your username or password is incorrect </div>')
        } 
        return render(request, 'index.html', context)

def reservasi(request):
    penumpang = request.POST['penumpang']
    lokasiawal = request.POST['lokasiawal']
    lokasiakhir = request.POST['lokasiakhir']
    tanggalreservasi = request.POST['date']
    bus = Bus.objects.get(lokasiawal = lokasiawal, lokasiakhir = lokasiakhir)
    #CREATE
    reservasi = Reservasi(penumpangid = penumpang, busid = bus.id, tanggalreservasi = tanggalreservasi)
    reservasi.save()
    akun = Penumpang.objects.get(id = penumpang)
    context = {
        'penumpang' : akun,
    }
    return render(request, 'homepage.html', context)

def jadwal(request, id):
    reservasi = Reservasi.objects.filter(penumpangid = id)
    tables = []
    for i in reservasi:
        bus = Bus.objects.get(id = i.busid)
        reservasi = Reservasi.objects.get(id = i.id)
        table = {
            'bus' : bus,
            'reservasi' : reservasi
        }
        tables.append(table)
    context = {
        'table' : tables,
    }
    return render(request, 'jadwal.html', context)

def hapus(request, id):
    reservasi = Reservasi.objects.get(id = id)
    penumpang = reservasi.penumpangid
    reservasi.delete()
    return redirect('/jadwal/' + str(penumpang) + '/')

def edit(request, id):
    reservasi = Reservasi.objects.get(id = id)
    context = {
        'reservasi' : reservasi,
    }
    return render(request, 'edit.html', context)

def update(request):
    reservasiid = request.POST['test']
    lokasiawal = request.POST['lokasiawal']
    lokasiakhir = request.POST['lokasiakhir']
    bus = Bus.objects.get(lokasiawal = lokasiawal, lokasiakhir = lokasiakhir)
    reservasi = Reservasi.objects.get(id=reservasiid)
    reservasi.busid = bus.id
    reservasi.save()
    return redirect('/jadwal/' + str(reservasi.penumpangid) + '/')

def register(request):
    return render(request, 'register.html')

def daftar(request):
    username = request.POST['username']
    password = request.POST['password']
    NIM = request.POST['NIM']
    penumpang = Penumpang(username = username, password = password, NIM = NIM)
    penumpang.save()
    context = {
        'penumpang' : penumpang,
    }
    return render(request, 'index.html', context)

def admin(request):
    return render(request, 'admin.html')

def adminlog(request):
    username = request.POST['username']
    password = request.POST['password']
    #SELECT * WHERE username = username, password = password
    admin = Admin.objects.get(username = username, password = password)
    reservasi = Reservasi.objects.all()
    tables = []
    for i in reservasi:
        bus = Bus.objects.get(id = i.busid)
        reservasi = Reservasi.objects.get(id = i.id)
        table = {
            'bus' : bus,
            'reservasi' : reservasi
        }
        tables.append(table)
    context = {
        'admin' : admin,
        'reservasi' : reservasi,
        'table' : tables,
    }
    return render(request, 'mainadmin.html', context)

def terima(request,id,admin):
    reservasi = Reservasi.objects.get(id = id)
    reservasi.statusreservasi = 'diterima'
    reservasi.save()
    admin = Admin.objects.get(id = admin)
    reservasi = Reservasi.objects.all()
    tables = []
    for i in reservasi:
        bus = Bus.objects.get(id = i.busid)
        reservasi = Reservasi.objects.get(id = i.id)
        table = {
            'bus' : bus,
            'reservasi' : reservasi
        }
        tables.append(table)
    context = {
        'admin' : admin,
        'reservasi' : reservasi,
        'table' : tables,
    }
    return render(request, 'mainadmin.html', context)

def tolak(request,id,admin):
    reservasi = Reservasi.objects.get(id = id)
    reservasi.statusreservasi = 'ditolak'
    reservasi.save()
    admin = Admin.objects.get(id = admin)
    reservasi = Reservasi.objects.all()
    tables = []
    for i in reservasi:
        bus = Bus.objects.get(id = i.busid)
        reservasi = Reservasi.objects.get(id = i.id)
        table = {
            'bus' : bus,
            'reservasi' : reservasi
        }
        tables.append(table)
    context = {
        'admin' : admin,
        'reservasi' : reservasi,
        'table' : tables,
    }
    return render(request, 'mainadmin.html', context)

def LogoutPage(request):
    logout(request)
    return redirect('index')