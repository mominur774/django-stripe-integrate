from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
