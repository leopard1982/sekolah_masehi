from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect

def welcome(request):
    return render(request,'welcome.html')
    # return HttpResponse('Hallo Selamat Pagi')

def testPage(request):
    return render(request,'test.html')
    # return HttpResponse('Hallo Selamat Pagi')
