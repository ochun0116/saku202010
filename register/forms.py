"""forms.py"""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserCreateForm(UserCreationForm):
    """ユーザー登録用フォーム"""

    class Meta:
        model = get_user_model()
        fields = ('email',)

    def clean_email(self):
        """clean_email"""
        email = self.cleaned_data['email']
        get_user_model().objects.filter(email=email, is_active=False).delete()
        return email

