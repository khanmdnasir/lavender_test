from django import forms
from django.db.models import fields
from .models import Mobile

class MobileForm(forms.ModelForm):
    brand_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    model=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    color=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    jan_code=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    image=forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
        model=Mobile
        fields='__all__'