from django.shortcuts import render, redirect
from index.models import *

def list_product(request):
    product = Product.objects.all()
    return render(request, "index/list_product.html", {"product": product})

def product(request, id): 
    product = Product.objects.get(id = id)
    return render(request, 'index/product.html', {"product": product})

def edit_product(request, id):
    if request.method == 'GET':
        try:
            global product
            product = Product.objects.get(id=id)
        except:
            product = None
        gr_product = GroupProduct.objects.all()
        return render(request, 'index/form_product.html', {"product": product, "gr_product": gr_product })
    if request.method == 'POST':
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
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/list_product')

def add_product(request):
    if request.method == "GET":
        gr_product = GroupProduct.objects.all()
        return render(request, 'index/form_product.html', {"gr_product": gr_product})
    if request.method == "POST":
        product = Product(
            name=request.POST['name'],
            price=request.POST['price'],
            quantity=request.POST['quantity'],
            group_id=request.POST['group']
        )
        product.save()
        return redirect('/list_product')