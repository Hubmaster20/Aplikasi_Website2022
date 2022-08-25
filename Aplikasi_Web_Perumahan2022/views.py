from .forms import Form_user
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .models import User, Model_kategori_perumahan, Model_vasilitas_perumahan, Model_perumahan, Model_kategori_kosan, Model_vasilitas_kosan, Model_kosan
import hashlib


def index(request):
	context = {
	'page_title':'Login',
	}
	#print(request.user)
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('Home')
		else:
			return redirect('index')

	return render(request, 'index.html',  context)

def HomeView(request):	
	context = {
	'page_title':'Home'
	}
	return render(request, 'home.html',  context)

def LogoutView(request):
	context = {
	'page_title':'logout',
	}
	if request.method == "POST":
		if request.POST["logout"] == "Submit":	
			logout(request)

		return redirect('index')

	return render(request, 'logout.html',  context)	


# data kategori perumahan
def Data_kategori_perumahan(request):
	tampil = Model_kategori_perumahan.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_kategori_perumahan/tabel.html',  context)	

def Tambah_kategori_perumahan(request):
	if request.method == 'POST':
		Model_kategori_perumahan.objects.create(
			nama_kategori = request.POST['nama_kategori'],
			tipe_perumahan = request.POST['tipe_perumahan'],
			keterangan = request.POST['keterangan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Kategori_perumahan/")	
	context = {	
	'Tambah': 'Tambah'
	}
	return render(request, 'Master_data/data_kategori_perumahan/tambah.html', context)

def Hapus_kategori_perumahan(request, hapus_kr):
	Model_kategori_perumahan.objects.filter(id=hapus_kr).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Kategori_perumahan')			

def Edit_kategori_perumahan(request, id_kr):		
	edit_data = Model_kategori_perumahan.objects.get(id=id_kr)
	if request.method == 'POST':		
			edit_data.nama_kategori = request.POST.get('nama_kategori')
			edit_data.tipe_perumahan = request.POST.get('tipe_perumahan')			
			edit_data.keterangan = request.POST.get('keterangan')	
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Kategori_perumahan')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_kategori_perumahan/edit.html',  context)

# vasilitas perumahan
def Data_vasilitas_perumahan(request):
	tampil = Model_vasilitas_perumahan.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_vasilitas_perumahan/tabel.html',  context)	

def Tambah_vasilitas_perumahan(request):
	if request.method == 'POST':
		Model_vasilitas_perumahan.objects.create(
			nama_vasilitas = request.POST['nama_vasilitas'],
			keterangan = request.POST['keterangan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Vasilitas_perumahan/")	
	context = {	
	'Tambah': 'Tambah',
	}
	return render(request, 'Master_data/data_vasilitas_perumahan/tambah.html', context)

def Hapus_vasilitas_perumahan(request, hapus_vsp):
	Model_vasilitas_perumahan.objects.filter(id=hapus_vsp).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Vasilitas_perumahan')			

def Edit_vasilitas_perumahan(request, id_vsp):		
	edit_data = Model_vasilitas_perumahan.objects.get(id=id_vsp)
	if request.method == 'POST':		
			edit_data.nama_vasilitas = request.POST.get('nama_vasilitas')			
			edit_data.keterangan = request.POST.get('keterangan')	
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Vasilitas_perumahan')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_vasilitas_perumahan/edit.html',  context)

# vasilitas perumahan
def Data_perumahan(request):
	tampil = Model_perumahan.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_perumahan/tabel.html',  context)	

def Tambah_perumahan(request):
	select_kategori = Model_kategori_perumahan.objects.all()
	select_vasilitas = Model_vasilitas_perumahan.objects.all()

	if request.method == 'POST':
		Model_perumahan.objects.create(
			nama_perumahan = request.POST['nama_perumahan'],
			nama_kategori = request.POST['nama_kategori'],
			tipe_perumahan = request.POST['tipe_perumahan'],
			luas = request.POST['luas'],
			alamat = request.POST['alamat'],
			nohp = request.POST['nohp'],
			deskripsi = request.POST['deskripsi'],
			foto_perumahan = request.FILES['foto_perumahan'],
			vasilitas = request.POST['vasilitas'],
			harga = request.POST['harga'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Perumahan/")	
	context = {	
	'Tambah': 'Tambah',
	'select_kategori': select_kategori,
	'select_vasilitas': select_vasilitas,
	}
	return render(request, 'Master_data/data_perumahan/tambah.html', context)

def Hapus_perumahan(request, hapus_pr):
	Model_perumahan.objects.filter(id=hapuspr).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Perumahan')			

def Edit_perumahan(request, id_pr):
	select_kategori = Model_kategori_perumahan.objects.all()
	select_vasilitas = Model_vasilitas_perumahan.objects.all()

	edit_data = Model_perumahan.objects.get(id=id_pr)
	if request.method == 'POST':		
			edit_data.nama_perumahan = request.POST.get('nama_perumahan')
			edit_data.nama_kategori = request.POST.get('nama_kategori')	
			edit_data.tipe_perumahan = request.POST.get('tipe_perumahan')	
			edit_data.luas = request.POST.get('luas')	
			edit_data.alamat = request.POST.get('alamat')	
			edit_data.nohp = request.POST.get('nohp')	
			edit_data.deskripsi = request.POST.get('deskripsi')	
			edit_data.foto_perumahan = request.FILES.get('foto_perumahan')	
			edit_data.vasilitas = request.POST.get('vasilitas')	
			edit_data.harga = request.POST.get('harga')	
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Perumahan')

	context = {
	'select_kategori': select_kategori,
	'select_vasilitas': select_vasilitas,
	'edit_data': edit_data
	}
	return render(request, 'Master_data/data_perumahan/edit.html',  context)


# kategori kosan
def Data_kategori_kosan(request):
	tampil = Model_kategori_kosan.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_kategori_kosan/tabel.html',  context)	

def Tambah_kategori_kosan(request):
	if request.method == 'POST':
		Model_kategori_kosan.objects.create(
			nama_kategori = request.POST['nama_kategori'],
			tipe_kosan = request.POST['tipe_kosan'],
			keterangan = request.POST['keterangan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Kategori_kosan/")	
	context = {	
	'Tambah': 'Tambah'
	}
	return render(request, 'Master_data/data_kategori_kosan/tambah.html', context)

def Hapus_kategori_kosan(request, hapus_ks):
	Model_kategori_kosan.objects.filter(id=hapus_ks).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Kategori_kosan')			

def Edit_kategori_kosan(request, id_ks):		
	edit_data = Model_kategori_kosan.objects.get(id=id_ks)
	if request.method == 'POST':		
			edit_data.nama_kategori = request.POST.get('nama_kategori')
			edit_data.tipe_kosan = request.POST.get('tipe_kosan')			
			edit_data.keterangan = request.POST.get('keterangan')	
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Kategori_kosan')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_kategori_kosan/edit.html',  context)


# vasilitas kosan
def Data_vasilitas_kosan(request):
	tampil = Model_vasilitas_kosan.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_vasilitas_kosan/tabel.html',  context)	

def Tambah_vasilitas_kosan(request):
	if request.method == 'POST':
		Model_vasilitas_kosan.objects.create(
			nama_vasilitas = request.POST['nama_vasilitas'],
			keterangan = request.POST['keterangan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Vasilitas_kosan/")	
	context = {	
	'Tambah': 'Tambah',
	}
	return render(request, 'Master_data/data_vasilitas_kosan/tambah.html', context)

def Hapus_vasilitas_kosan(request, hapus_ksn):
	Model_vasilitas_kosan.objects.filter(id=hapus_ksn).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Vasilitas_kosan')			

def Edit_vasilitas_kosan(request, id_ksn):		
	edit_data = Model_vasilitas_kosan.objects.get(id=id_ksn)
	if request.method == 'POST':		
			edit_data.nama_vasilitas = request.POST.get('nama_vasilitas')			
			edit_data.keterangan = request.POST.get('keterangan')	
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Vasilitas_kosan')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_vasilitas_kosan/edit.html',  context)


# kosan
def Data_kosan(request):
	tampil = Model_kosan.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_kosan/tabel.html',  context)	

def Tambah_kosan(request):
	select_kategori = Model_kategori_kosan.objects.all()
	select_vasilitas = Model_vasilitas_kosan.objects.all()

	if request.method == 'POST':
		Model_kosan.objects.create(
			nama_kosan = request.POST['nama_kosan'],
			nama_kategori = request.POST['nama_kategori'],
			tipe_kosan = request.POST['tipe_kosan'],
			luas = request.POST['luas'],
			alamat = request.POST['alamat'],
			nohp = request.POST['nohp'],
			deskripsi = request.POST['deskripsi'],
			foto_kosan = request.FILES['foto_kosan'],
			vasilitas = request.POST['vasilitas'],
			harga = request.POST['harga'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Kosan/")	
	context = {	
	'Tambah': 'Tambah',
	'select_kategori': select_kategori,
	'select_vasilitas': select_vasilitas,
	}
	return render(request, 'Master_data/data_kosan/tambah.html', context)

def Hapus_kosan(request, hapus_ksn):
	Model_kosan.objects.filter(id=hapus_ksn).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Kosan')			

def Edit_kosan(request, id_ksn):
	select_kategori = Model_kategori_kosan.objects.all()
	select_vasilitas = Model_vasilitas_kosan.objects.all()

	edit_data = Model_kosan.objects.get(id=id_ksn)
	if request.method == 'POST':		
			edit_data.nama_kosan = request.POST.get('nama_kosan')
			edit_data.nama_kategori = request.POST.get('nama_kategori')	
			edit_data.tipe_kosan = request.POST.get('tipe_kosan')	
			edit_data.luas = request.POST.get('luas')	
			edit_data.alamat = request.POST.get('alamat')	
			edit_data.nohp = request.POST.get('nohp')	
			edit_data.deskripsi = request.POST.get('deskripsi')	
			edit_data.foto_kosan = request.FILES.get('foto_kosan')	
			edit_data.vasilitas = request.POST.get('vasilitas')	
			edit_data.harga = request.POST.get('harga')	
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Kosan')

	context = {
	'select_kategori': select_kategori,
	'select_vasilitas': select_vasilitas,
	'edit_data': edit_data
	}
	return render(request, 'Master_data/data_kosan/edit.html',  context)


# halaman website
def Halaman_kosan(request):
	tampil_kosan = Model_kosan.objects.all()
	tampil_perumahan = Model_perumahan.objects.all()
	# select data
	select_perumahan = Model_kategori_perumahan.objects.all()
	select_kosan = Model_kategori_kosan.objects.all()
	# vasilitas
	select_vasilitas_perumahan = Model_vasilitas_perumahan.objects.all()
	select_vasilitas_kosan = Model_vasilitas_kosan.objects.all()
	context = {	
	'tampil_kosan': tampil_kosan,
	'tampil_perumahan': tampil_perumahan,
	'select_perumahan': select_perumahan,
	'select_kosan': select_kosan,
	'select_vasilitas_kosan': select_vasilitas_kosan,
	'select_vasilitas_perumahan': select_vasilitas_perumahan
	}
	return render(request, 'Website/halaman_kosan.html',  context)	
# cari kosan
def cari_kosan(request):
	if 'cari_kosan' in request.GET:
		cari_kosan=request.GET['cari_kosan']
		tampil_kosan = Model_kosan.objects.filter(nama_kategori=cari_kosan)
	else:
		tampil_kosan = Model_kosan.objects.filter(nama_kategori=None)
	# select data
	select_perumahan = Model_kategori_perumahan.objects.all()
	select_kosan = Model_kategori_kosan.objects.all()
	# vasilitas
	select_vasilitas_perumahan = Model_vasilitas_perumahan.objects.all()
	select_vasilitas_kosan = Model_vasilitas_kosan.objects.all()
	context = {	
	'tampil_kosan': tampil_kosan,
	'select_perumahan': select_perumahan,
	'select_kosan': select_kosan,
	'select_vasilitas_kosan': select_vasilitas_kosan,
	'select_vasilitas_perumahan': select_vasilitas_perumahan
	}
	return render(request, 'Website/cari_kosan.html',  context)

# detail kosan
def detail_kosan(request):
	if 'cari_kosan' in request.GET:
		cari_kosan=request.GET['cari_kosan']
		tampil_kosan = Model_kosan.objects.filter(id=cari_kosan)
	else:
		tampil_kosan = Model_kosan.objects.filter(id=None)
	# select data
	select_perumahan = Model_kategori_perumahan.objects.all()
	select_kosan = Model_kategori_kosan.objects.all()
	# vasilitas
	select_vasilitas_perumahan = Model_vasilitas_perumahan.objects.all()
	select_vasilitas_kosan = Model_vasilitas_kosan.objects.all()
	context = {	
	'tampil_kosan': tampil_kosan,
	'select_perumahan': select_perumahan,
	'select_kosan': select_kosan,
	'select_vasilitas_kosan': select_vasilitas_kosan,
	'select_vasilitas_perumahan': select_vasilitas_perumahan
	}
	return render(request, 'Website/detail_kosan.html',  context)

def cari_vasilitas_kosan(request):
	if 'cari_vasilitas_kosan' in request.GET:
		cari_vasilitas_kosan=request.GET['cari_vasilitas_kosan']
		tampil_kosan = Model_kosan.objects.filter(vasilitas=cari_vasilitas_kosan)
	else:
		tampil_kosan = Model_kosan.objects.filter(vasilitas=None)
	# select data
	select_perumahan = Model_kategori_perumahan.objects.all()
	select_kosan = Model_kategori_kosan.objects.all()
	# vasilitas
	select_vasilitas_perumahan = Model_vasilitas_perumahan.objects.all()
	select_vasilitas_kosan = Model_vasilitas_kosan.objects.all()
	context = {	
	'tampil_kosan': tampil_kosan,
	'select_perumahan': select_perumahan,
	'select_kosan': select_kosan,
	'select_vasilitas_kosan': select_vasilitas_kosan,
	'select_vasilitas_perumahan': select_vasilitas_perumahan
	}
	return render(request, 'Website/vasilitas_kosan.html',  context)


# cari perumahan
def cari_perumahan(request):
	if 'cari_perumahan' in request.GET:
		cari_perumahan=request.GET['cari_perumahan']
		tampil_perumahan = Model_perumahan.objects.filter(nama_kategori=cari_perumahan)
	else:
		tampil_perumahan = Model_perumahan.objects.filter(nama_kategori=None)
	# select data
	select_perumahan = Model_kategori_perumahan.objects.all()
	select_kosan = Model_kategori_kosan.objects.all()
	# vasilitas
	select_vasilitas_perumahan = Model_vasilitas_perumahan.objects.all()
	select_vasilitas_kosan = Model_vasilitas_kosan.objects.all()
	context = {	
	'tampil_perumahan': tampil_perumahan,
	'select_perumahan': select_perumahan,
	'select_kosan': select_kosan,
	'select_vasilitas_kosan': select_vasilitas_kosan,
	'select_vasilitas_perumahan': select_vasilitas_perumahan
	}
	return render(request, 'Website/cari_perumahan.html',  context)


# detail perumahan
def detail_perumahan(request):
	if 'cari_perumahan' in request.GET:
		cari_perumahan=request.GET['cari_perumahan']
		tampil_perumahan = Model_perumahan.objects.filter(id=cari_perumahan)
	else:
		tampil_perumahan = Model_perumahan.objects.filter(id=None)
	# select data
	select_perumahan = Model_kategori_perumahan.objects.all()
	select_kosan = Model_kategori_kosan.objects.all()
	# vasilitas
	select_vasilitas_perumahan = Model_vasilitas_perumahan.objects.all()
	select_vasilitas_kosan = Model_vasilitas_kosan.objects.all()
	context = {	
	'tampil_perumahan': tampil_perumahan,
	'select_perumahan': select_perumahan,
	'select_kosan': select_kosan,
	'select_vasilitas_kosan': select_vasilitas_kosan,
	'select_vasilitas_perumahan': select_vasilitas_perumahan
	}
	return render(request, 'Website/detail_perumahan.html',  context)

# vasilitas perumahan
def cari_vasilitas_perumahan(request):
	if 'cari_vasilitas_perumahan' in request.GET:
		cari_vasilitas_perumahan=request.GET['cari_vasilitas_perumahan']
		tampil_perumahan = Model_perumahan.objects.filter(vasilitas=cari_vasilitas_perumahan)
	else:
		tampil_perumahan = Model_perumahan.objects.filter(vasilitas=None)
	# select data
	select_perumahan = Model_kategori_perumahan.objects.all()
	select_kosan = Model_kategori_kosan.objects.all()
	# vasilitas
	select_vasilitas_perumahan = Model_vasilitas_perumahan.objects.all()
	select_vasilitas_kosan = Model_vasilitas_kosan.objects.all()
	context = {	
	'tampil_perumahan': tampil_perumahan,
	'select_perumahan': select_perumahan,
	'select_kosan': select_kosan,
	'select_vasilitas_kosan': select_vasilitas_kosan,
	'select_vasilitas_perumahan': select_vasilitas_perumahan
	}
	return render(request, 'Website/vasilitas_perumahan.html',  context)



# laporan
def LP_perumahan(request):
	tampil = Model_perumahan.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/laporan/lp_perumahan.html',  context)	

def LP_kosan(request):
	tampil = Model_kosan.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/laporan/lp_kosan.html',  context)	