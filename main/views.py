from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm

def show_main(request):
    products = Product.objects.all()
    context = {
        'npm' : '2406418995',
        'name': 'Khalisa Adzkiyah',
        'class': 'PBP A',
        'products': products,
    }
    return render(request, "main/main.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Tambah produk baru
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:show_main') # balik ke halaman utama setelah tambah produk
    else:
        form = ProductForm()
    return render(request, "main/add_product.html", {'form': form})

# Detail produk
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "main/product_detail.html", {'product': product})


