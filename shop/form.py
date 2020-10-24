from django import forms
from .models import Discussion


class DiscussionForm(forms.ModelForm):
    """DiscussionForm"""
    class Meta:
        model = Discussion
        exclude = ('product_id', 'created_at')
        fields = ('chat',)
