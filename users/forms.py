from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordResetForm, UserCreationForm

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'country', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class ChangePasswordForm(PasswordResetForm):
    email = forms.EmailField(
        label='Email', max_length=254, widget=forms.EmailInput(
            attrs={'autocomplete': 'email', 'class': 'form-control', 'placeholder': 'Введите ваш email'}))
