from django.contrib.auth import forms

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')