

from django import forms
from .models import Shoe, Brand

class ShoeForm(forms.ModelForm):
    brand= forms.ModelChoiceField(queryset=Brand.objects.all(), widget=forms.Select(attrs={'placeholder': 'Select a brand'}))
    model = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Model'}))
    size = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Size'}))
    price = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Price'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': 'Choose a photo'}))


    class Meta:
        model = Shoe
        fields = '__all__'
