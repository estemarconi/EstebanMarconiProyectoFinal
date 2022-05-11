from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import SignUpForm, LoginForm, EditProfileForm
from .models import User, Profile

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Felicitaciones, se ha registrado satisfactoriamente")
            return redirect('Inicio')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return redirect('Inicio')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            # We check if the data is correct
            user = authenticate(email=email, password=password)
            if user:  # If the returned object is not None
                auth_login(request, user)  # we connect the user
                return redirect('Inicio')
            else:  # otherwise an error will be displayed
                messages.error(request, 'Correo o contraseña erronea')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect(reverse('accounts:login'))

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {'user': user})

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            about_me = form.cleaned_data["about_me"]
            username = form.cleaned_data["username"]
            image = form.cleaned_data["image"]

            user = User.objects.get(id=request.user.id)
            profile = Profile.objects.get(user=user)
            user.username = username
            user.save()
            profile.about_me = about_me
            if image:
                profile.image = image
            profile.save()
            return redirect("accounts:profile", username=user.username)
    else:
        form = EditProfileForm()
    return render(request, "users/edit_profile.html", {'form': form})