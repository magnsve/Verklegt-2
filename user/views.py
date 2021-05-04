from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from user.decorators import admin_required
from user.forms.profile_form import ProfileForm, ProfileUpdateForm
from user.models import Profile


def index(request):
    return render(request, 'user/index.html')


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


def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile)
    })


@login_required
@admin_required
def update_profile(request, id):
    instance = get_object_or_404(Profile, pk=id)
    if request.method == 'POST':
        form = ProfileUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('update_profile', id=id)
    else:
        form = ProfileUpdateForm(instance=instance)
    return render(request, 'user/update_profile.html', {
        'form': form,
        'id': id
    })