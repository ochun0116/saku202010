"""urls.py"""
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('mypage/', views.MyPage.as_view(), name='mypage'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('detail/discussion/create/', views.DiscussionCreateView.as_view(), name='discussion_create'),
]
