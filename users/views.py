from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CreationForm
from profiles.models import CustomerProfile, PerformerProfile


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('users:main')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()

        user_type = form.cleaned_data['user_type']

        if user_type == 'CU':
            CustomerProfile.objects.create(name=user)
        elif user_type == 'PE':
            PerformerProfile.objects.create(name=user)

        return super().form_valid(form)


def main(request):
    return render(request, 'base.html')
