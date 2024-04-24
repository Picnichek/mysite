from django import forms
from .models import CustomerProfile, PerformerProfile


class PerformerProfileForm(forms.ModelForm):
    class Meta:
        model = PerformerProfile
        fields = ['contact_info', 'experience']


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['contact_info', 'experience']
