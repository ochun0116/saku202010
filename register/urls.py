"""urls.py"""
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'register'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user_create/', views.UserCreate.as_view(), name='user_create'),
    path('user_create/done', views.UserCreateDone.as_view(), name='user_create_done'),
    path('user_create/complete/<str:token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),
]
