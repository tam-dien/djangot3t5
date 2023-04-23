from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def handler404(request, exception):
    return HttpResponse("Bạn đang vào 1 đường dẫn sai")

def list_product(request):
    product = Product.objects.all()
    return render(request,"list_product.html",{"product":product})

def edit_product(request,id):
    if request.method == "GET":
        try:
            product = Product.objects.get(id=id)
        except:
            product = None
        gr_product = GroupProduct.objects.all()
        return render(request,"form_product.html",{"product":product,"gr_product":gr_product})
    if request.method == "POST":
        product = Product.objects.get(id=id)
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.quantity = request.POST['quantity']
        product.group_id = request.POST['group']
        product.save()
        return redirect("/list_product")

def delete_product(request,id):
    return redirect("/list_product")

def add_product(request):
    if request.method == "GET":
        gr_product = GroupProduct.objects.all()
        return render(request,"form_product.html",{"gr_product":gr_product})
    if request.method == "POST":
        product = Product(
            name=request.POST['name'],
            price=request.POST['price'],
            quantity=request.POST['quantity'],
            group_id=request.POST['group'],
        )
        product.save()
        return redirect("/list_product")