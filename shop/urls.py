"""urls.py"""
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('mypage/', views.MyPage.as_view(), name='mypage'),
    path('mypage/register/', views.ProductRegister.as_view(), name='product_register'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('detail/<int:pk>/discussion/<int:user>/create/', views.DiscussionCreateView.as_view(),
         name='discussion_create'),
]
