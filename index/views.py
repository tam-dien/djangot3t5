from django.shortcuts import render, redirect
from index.models import *

def list_product(request):
    product = Product.objects.all()
    return render(request, "index/list_product.html", {"product": product})

def edit_product(request, id):
    product = Product.objects.get(id=id)
    gr_product = GroupProduct.objects.all()
    if request.method == 'GET':
        return render(request, 'index/edit_product.html', {"product": product, "gr_product": gr_product })
    elif request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        group = request.POST.get('group')
        if group == "": group = None
        product.name = name
        product.price = price
        product.quantity = quantity
        product.group = GroupProduct.objects.get(id=group)
        product.save()
        return redirect(f'/product/{id}')

def delete_product(request, id):
    return redirect('/list_product')