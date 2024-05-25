from django.shortcuts import render, redirect,get_object_or_404
from .models import Shoe,Store
from .forms import ShoeForm


def index(request):
    store_list = Store.objects.all()  
    return render(request, 'www/index.html', {'store_list':store_list})

def shoe(request):
    if request.method == 'POST':
        form = ShoeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shoe')
    else:
        form = ShoeForm()
    
    shoes = Shoe.objects.all()
    return render(request, 'www/shoe.html', {'shoes': shoes, 'shoe_form': form})

def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    shoe_list = Shoe.objects.all()

    if request.method == 'POST':
        shoe_id = request.POST.get('shoe_id')
        shoe = get_object_or_404(Shoe, id=shoe_id)
        store.shoes.add(shoe)  # Dodawanie buta do sklepu

    added_shoe_list = store.shoes.all()  # Pobieranie listy dodanych butów w sklepie

    return render(request, 'www/store_detail.html', { 'store': store, 'shoe_list': shoe_list, 'added_shoe_list': added_shoe_list })