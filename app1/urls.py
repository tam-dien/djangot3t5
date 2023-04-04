from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.index),
    path('hi/', views.hi),
    path('sanpham/<int:id>', views.sanpham),
    path('danhsachsanpham/<int:id>', views.danhsachsanpham),
    path('sanpham2/<int:group>/<int:id>', views.sanpham2),
    path('test_request/', views.test_request),
    path('timsp/', views.timsp),
    path('login/', views.login),
    path('add_product/<int:group>', views.add_product),
]
