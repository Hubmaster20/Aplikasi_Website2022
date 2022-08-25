from django.contrib import admin

# Register your models here. daftar model yang telah kita buat
from .models import Model_kategori_perumahan, Model_vasilitas_perumahan, Model_perumahan, Model_kategori_kosan, Model_vasilitas_kosan, Model_kosan

admin.site.register(Model_kategori_kosan)
admin.site.register(Model_vasilitas_kosan)
admin.site.register(Model_kosan)
admin.site.register(Model_kategori_perumahan)
admin.site.register(Model_vasilitas_perumahan)
admin.site.register(Model_perumahan)