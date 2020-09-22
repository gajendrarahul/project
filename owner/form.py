from django import forms
from .models import Owner

class AddOwner(forms.ModelForm):
    owner_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    bike_no = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    license_no = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    blood_group = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_tax_paid = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Owner
        fields = ['owner_name', 'bike_no', 'licence_no', 'blood_group', 'last_tax_paid']