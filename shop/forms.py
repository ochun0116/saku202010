from django import forms
from django.db.models import Count

from .models import Discussion, Product, Category


class DiscussionForm(forms.ModelForm):
    """DiscussionForm"""
    class Meta:
        model = Discussion
        exclude = ('product_id', 'created_at')
        fields = ('chat',)


class ProductRegisterForm(forms.ModelForm):
    """ProductRegisterForm"""
    class Meta:
        model = Product
        exclude = ('user_id', 'created_at')
        fields = ('category', 'name', 'price', 'description', 'image')


class SearchForm(forms.Form):
    """検索フォーム"""
    keyword = forms.CharField(
        label='キーワード',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '検索キーワード'})
    )

    category = forms.ModelChoiceField(
        label='カテゴリ',
        required=False,
        queryset=Category.objects.annotate(product_count=Count('product')),
        widget=forms.RadioSelect,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        all_product_count = Product.objects.filter(inactive=False).count()
        self.fields['category'].empty_label = f'全カテゴリ({all_product_count})'
