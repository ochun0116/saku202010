from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from .models import Product, Discussion


class Index(generic.TemplateView):
    template_name = 'shop/index.html'


class MyPage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'shop/mypage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(user=self.request.user).order_by('created_at')
        context['discussions'] = Discussion.objects.filter(product__user=self.request.user).order_by('created_at')

        return context
