from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm, UserRegisterForm
from django.contrib.auth import login

def homepage(request):
    return render(request,'user_management/homepage.html')

def register(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)

        if register_form.is_valid():
            user = register_form.save()

            Profile.objects.create(
                user=user,
                name=register_form.cleaned_data.get('username'),
                email=register_form.cleaned_data.get('email')
            )
            login(request, user)

            return redirect('user_management:home')
    else:
        register_form = UserRegisterForm()

    return render(request, 'user_management/register.html', {'register_form': register_form})

def password_reset(request):
    return render(request, 'user_management/forgetPassword.html')

@login_required
def update_profile(request):
    account, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=account)

        if profile_form.is_valid():
            profile = profile_form.save()
            request.user.email = profile.email
            
            request.user.save()
            return redirect('user_management:update_profile')
        
    else:
        profile_form = ProfileForm(instance=account)

    return render(request, 'user_management/profile.html', {'account': account , 'profile_form': profile_form})