from django.shortcuts import render, redirect
from .models import Shoe
from .forms import ShoeForm

def index(request):
    if request.method == 'POST':
        form = ShoeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ShoeForm()
    
    shoes = Shoe.objects.all()
    return render(request, 'www/index.html', {'shoes': shoes, 'shoe_form': form})
