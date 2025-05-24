from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.

def LoginUser(request):

    if request.method == "POST":
        form = LoginUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username,password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'Şifre veya kullanıcı adı hatalı')
    else:
        form = LoginUserForm()
        
    return render(request, 'giris.html', {'form':form})

def RegisterUser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            # UserCreationForm, password1 ve password2'yi otomatik olarak doğruluyor.
            user = form.save()  # form.save() ile kullanıcıyı kaydet
            login(request, user)  # Kullanıcı kaydolduktan sonra giriş yap
            return redirect('login')  # Kayıt sonrası ana sayfaya yönlendir
    else:
        form = RegisterUserForm()

    return render(request, 'kayıt.html', {'form':form})

def home(request):
    return render(request, 'home.html')

def Profil(request):
    return render(request, 'profile.html')


