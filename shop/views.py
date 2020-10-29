from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import CreateView

from .forms import DiscussionForm, ProductRegisterForm
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


class DiscussionCreateView(LoginRequiredMixin, CreateView):
    """DiscussionCreateView"""
    model = Discussion
    template_name = "shop/discussions/create.html"
    form_class = DiscussionForm

    def form_valid(self, form):
        form.instance.product_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('shop:product_detail', kwargs={'pk': self.kwargs.get('pk')})


class ProductRegister(LoginRequiredMixin, CreateView):
    """ProductCreateView"""
    model = Product
    template_name = "shop/product/create.html"
    form_class = ProductRegisterForm
    success_url = reverse_lazy("shop:mypage")

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)
