from django.db import models
import os
from django.conf import settings

# Create your models here.
class Student(models.Model):
    id = models.CharField(max_length=100,primary_key=True,null=False,blank=False,default="id1",verbose_name="ID Siswa")
    nama = models.CharField(max_length=100,blank=False,null=False,default="name",verbose_name="Nama Siswa")
    foto = models.ImageField(upload_to='siswa', verbose_name="Foto Siswa")

    def __str__(self):
        return f"{self.nama}"
    
    def save(self,*args,**kwargs):
        file_lama = str(Student.objects.get(id=self.id).foto)
        try:
            os.remove(os.path.join(settings.BASE_DIR,'media\\' + file_lama))
        except Exception as ex:
            print(f"error: {ex}")
        super(Student,self).save(*args,**kwargs)