from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect
import os
from django.conf import settings

def welcome(request):
    return render(request,'welcome.html')
    # return HttpResponse('Hallo Selamat Pagi')

def testPage(request):
    return render(request,'test.html')
    # return HttpResponse('Hallo Selamat Pagi')

def tentangKami(request):
    return render(request,'section/kami.html')

def blogsSection(request,id):
    if id=="1":
        return render(request,'blogs/html1.html')
    else:
        return render(request,'section/kami.html')
    
def blogsList(request):
    lokasi_base_path = str(settings.BASE_DIR)
    lokasi_template = '\\templates\\blogs\\'
    gabungan_lokasi = lokasi_base_path+lokasi_template
    
    #simpan daftar template ke dalam list []
    list_template = os.listdir(gabungan_lokasi)
    
    #simpan list hanya untuk filename tanpa extension ke dalam list[]
    list_data = []
    for list in list_template:
        #simpan nama file, hilangkan extension dan dapatkan data split di indeks ke 0
        filename = list.split('.')[0]
        #tambahkan ke list tanpa ada extension (ditambahkan nanti di template pakai context)
        list_data.append(filename)

    print(list_data)
    context = {
        'list_data':list_data
    }

    return render(request,'section/blogs.html',context)
