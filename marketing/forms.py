from django import forms
from .models import Customer, Campaign  # Adjust the import based on your project structure

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'  # You can specify the fields you want to include in the form here

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = '__all__'
