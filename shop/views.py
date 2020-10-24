from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
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
    success_url = reverse_lazy("shop:index")

    def form_valid(self, form):
        product_pk = self.request.user.id
        comment = form.save(commit=False)
        comment.product_id = product_pk
        comment.save()
        return redirect('shop:product_detail', pk=product_pk)


class ProductRegister(LoginRequiredMixin, CreateView):
    """ProductCreateView"""
    model = Product
    template_name = "shop/product/create.html"
    form_class = ProductRegisterForm
    success_url = reverse_lazy("shop:mypage")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
