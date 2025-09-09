from django.shortcuts import render
from .models import Product

def show_main(request):
    products = Product.objects.all()
    context = {
        'npm' : '2406418995',
        'name': 'Khalisa Adzkiyah',
        'class': 'PBP A',
        'products': products,
    }
    return render(request, "main/main.html", context)

