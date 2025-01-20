from django.urls import path
from .views import indeks, tentangKami,blogsSection,blogsList

urlpatterns = [
    path('', indeks, name='welcome'),
    path('kami/',tentangKami,name='tentang_kami'),
    path('blogs/<str:id>/',blogsSection,name="blogs_section"),
    path('blogs/',blogsList,name='blogs_list')
]
