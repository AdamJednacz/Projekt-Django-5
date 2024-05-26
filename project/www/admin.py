from django import forms
from django.contrib import admin
from .models import Shoe, Store, Brand

class StoreAdminForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'
    
    shoes = forms.ModelMultipleChoiceField(queryset=Shoe.objects.all(),required=False, widget=admin.widgets.FilteredSelectMultiple('Shoes', is_stacked=False))

class StoreAdmin(admin.ModelAdmin):
    form = StoreAdminForm

admin.site.register(Shoe)
admin.site.register(Store, StoreAdmin)
admin.site.register(Brand)
