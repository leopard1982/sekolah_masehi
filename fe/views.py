from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect

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
