from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

def homepage(request):
    return render(request,'user_management/homepage.html')

@login_required
def update_profile(request):
    account, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profileForm = ProfileForm(request.POST, instance=account)

        if profileForm.is_valid():
            profile = profileForm.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('user_management:update_profile')
        
    else:
        profileForm = ProfileForm(instance=account)

    return render(request, 'user_management/profile.html', {'account': account , 'profile': profileForm})