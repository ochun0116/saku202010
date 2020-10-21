"""urls.py"""
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('mypage/', views.MyPage.as_view(), name='mypage'),
]
