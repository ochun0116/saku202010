from django.urls import path

# 現在のフォルダの「views.py」を import する！さっき "Hello, world." したやつ！
from . import views

# views.py には「index」という関数を作りましたね！それを呼んでます
urlpatterns = [
    path('', views.index, name='index'),
]
