from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Model_kategori_perumahan(models.Model):
	nama_kategori	= models.CharField(max_length = 1200)
	tipe_perumahan	=models.CharField(max_length = 1200)
	keterangan	=models.CharField(max_length = 25)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_kategori)

class Model_vasilitas_perumahan(models.Model):
	nama_vasilitas	= models.CharField(max_length = 1200)
	keterangan	=models.CharField(max_length = 25)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_vasilitas)

class Model_perumahan(models.Model):
	nama_perumahan	= models.CharField(max_length = 1200)
	nama_kategori	= models.CharField(max_length = 1200)
	tipe_perumahan	=models.CharField(max_length = 1200)
	luas	=models.CharField(max_length = 25)	
	alamat	= models.CharField(max_length = 1200)
	nohp	= models.CharField(max_length = 1200)
	deskripsi	= models.CharField(max_length = 1200)
	foto_perumahan	=models.ImageField(upload_to ='Berkas/', null=True)	
	vasilitas	= models.CharField(max_length = 1200)
	harga	= models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_perumahan)


# kosan
class Model_kategori_kosan(models.Model):
	nama_kategori	= models.CharField(max_length = 1200)
	tipe_kosan	=models.CharField(max_length = 1200)
	keterangan	=models.CharField(max_length = 25)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_kategori)

class Model_vasilitas_kosan(models.Model):
	nama_vasilitas	= models.CharField(max_length = 1200)	
	keterangan	=models.CharField(max_length = 25)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_vasilitas)

class Model_kosan(models.Model):
	nama_kosan	= models.CharField(max_length = 1200)
	nama_kategori	= models.CharField(max_length = 1200)
	tipe_kosan	=models.CharField(max_length = 1200)
	luas	=models.CharField(max_length = 25)
	alamat	= models.CharField(max_length = 1200)
	nohp	= models.CharField(max_length = 1200)
	deskripsi	= models.CharField(max_length = 1200)
	foto_kosan	=models.ImageField(upload_to ='Berkas/', null=True)	
	vasilitas	= models.CharField(max_length = 1200)
	harga	= models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_kosan)