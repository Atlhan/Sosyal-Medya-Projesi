from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginUserForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı", widget=forms.TextInput(attrs={
        'class':'form-control',
        'size':35
        }))
    password = forms.CharField(label="Şifre", widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'size':35
        }))

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Kullanıcı Adınız", widget=forms.TextInput(attrs={
        'class':'form-control',
        'size':35
        }))
    password1 = forms.CharField(label="Şifre", widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'size':35
        }))
    password2 = forms.CharField(label="Şifre Tekrar", widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'size':35
        }))

    class Meta:
        model = User
        fields = ['username','password1','password2']