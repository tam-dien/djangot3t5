from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("đây là hàm index ở app 1")

def hi(request):
    return HttpResponse("đây là hàm hi ở app 1")