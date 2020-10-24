from django import forms
from .models import Discussion, Product


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
        fields = ('name', 'category',)
