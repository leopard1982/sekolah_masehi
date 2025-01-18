from django.urls import path
from .views import welcome, testPage

urlpatterns = [
    path('', welcome, name='welcome'),
    path('test/',testPage,name='test_page')
]
