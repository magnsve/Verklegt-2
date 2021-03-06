from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from ship_o_cereal.decorators import admin_required
from user.forms.profile_form import ProfileForm, ProfileUpdateForm
from user.models import Profile, SearchHistory


def index(request):
    return render(request, 'user/index.html')


#Create user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


def logout_redirect(request):
    return render(request, 'user/logout_redirect.html')


#User profile with search history
def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if profile is None:
        profile = Profile(user_id=request.user.id)
        profile.save()
    print(profile)
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    today = date.today()
    yesterday = today - timedelta(1)
    lastweek = today - timedelta(7)
    context = {
        'form': ProfileForm(instance=profile),
        'today': SearchHistory.objects.filter(profile=request.user.profile, timestamp=today).order_by('-timestamp'),
        'yesterday': SearchHistory.objects.filter(profile=request.user.profile,timestamp=yesterday).order_by('-timestamp'),
        'lastweek': SearchHistory.objects.filter(profile=request.user.profile, timestamp__lt=yesterday,timestamp__gte=lastweek).order_by('-timestamp'),
        'older': SearchHistory.objects.filter(profile=request.user.profile, timestamp__lt=lastweek).order_by('-timestamp'),
    }
    return render(request, 'user/profile.html', context)






