from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import CreateView

from .forms import DiscussionForm, ProductRegisterForm, SearchForm
from .models import Product, Discussion, Category


class ProductListView(generic.ListView):
    """ / で product 一覧."""
    model = Product
    queryset = Product.objects.filter(inactive=False)
    ordering = '-created_at'

    def get_queryset(self):
        """検索された結果を返します"""
        queryset = super().get_queryset()
        self.form = SearchForm(self.request.GET or None)
        if self.form.is_valid():
            category = self.form.cleaned_data.get('category')
            if category:
                queryset = queryset.filter(category=category)

            keyword = self.form.cleaned_data['keyword']
            if keyword:
                queryset = queryset.filter(Q(name__icontains=keyword)).distinct()

        return queryset.select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form
        return context


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
        form.instance.category_id = Category.objects.filter(name=form.cleaned_data["category"]).values("id")
        return super().form_valid(form)
