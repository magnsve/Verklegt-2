from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from ship_o_cereal.decorators import admin_required
from user.forms.profile_form import ProfileUpdateForm
from user.models import Profile


def index(request):
    return render(request, 'administrate/index.html')


def administrate_products(request):
    return render(request, 'administrate/administrate_products.html')


@login_required
@admin_required
def administrate_users(request, id):
    context = {'profiles': Profile.objects.exclude(user_id=id)}
    return render(request, 'administrate/administrate_users.html', context)

@login_required
@admin_required
def update_profile(request, id):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileUpdateForm(data=request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('update_profile', id=id)
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'administrate/update_profile.html', {
        'form': form,
        'id': id
    })