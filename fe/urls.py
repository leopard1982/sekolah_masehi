from django.urls import path
from .views import welcome, testPage, tentangKami,blogsSection

urlpatterns = [
    path('', welcome, name='welcome'),
    path('test/',testPage,name='test_page'),
    path('kami/',tentangKami,name='tentang_kami'),
    path('blogs/<str:id>/',blogsSection,name="blogs_section")
]
