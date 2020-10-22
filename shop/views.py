from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Product, Discussion


class ProductListView(generic.ListView):
    """ / で product 一覧."""
    model = Product


class ProductDetailView(generic.DetailView):
    """/detail/post_pk でアクセス。product 詳細."""
    model = Product


class MyPage(LoginRequiredMixin, generic.TemplateView):
    """/mypage でアクセス。マイページ"""
    template_name = 'shop/mypage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(user=self.request.user).order_by('created_at')
        context['discussions'] = Discussion.objects.filter(product__user=self.request.user).order_by('created_at')

        return context
