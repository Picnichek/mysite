from django.shortcuts import render, redirect

from .models import CustomerProfile, PerformerProfile
from .forms import CustomerProfileForm, PerformerProfileForm


def customer_profile(request):
    performer = request.user.customerprofile
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=performer)
        if form.is_valid():
            form.save()
            return redirect('profiles:customer_profile')
    else:
        form = CustomerProfileForm(instance=performer)
    return render(request, 'profiles/customer_profile.html', {'form': form})


def performer_profile(request):
    performer = request.user.performerprofile
    if request.method == 'POST':
        form = PerformerProfileForm(request.POST, instance=performer)
        if form.is_valid():
            form.save()
            return redirect('profiles:performer_profile')
    else:
        form = PerformerProfileForm(instance=performer)
    return render(request, 'profiles/performer_profile.html', {'form': form})
