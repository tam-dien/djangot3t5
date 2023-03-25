from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.index),
    path('hi/', views.hi),
    path('sanpham/<int:id>', views.sanpham),
    path('danhsachsanpham/<int:id>', views.danhsachsanpham),
]
