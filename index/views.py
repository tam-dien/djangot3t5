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
        return render(request,"edit_product.html",{})

def delete_product(request,id):
    return redirect("/list_product")