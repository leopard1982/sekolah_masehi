from django.urls import path
from .views import welcome, testPage, tentangKami,blogsSection,blogsList

urlpatterns = [
    path('', welcome, name='welcome'),
    path('test/',testPage,name='test_page'),
    path('kami/',tentangKami,name='tentang_kami'),
    path('blogs/<str:id>/',blogsSection,name="blogs_section"),
    path('blogs/',blogsList,name='blogs_list')
]
