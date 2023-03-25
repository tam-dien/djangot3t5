from django.urls import path
from index import views

urlpatterns = [
    path('', views.index),
    path('xulytime/', views.xulytime),
    path('link1/', views.link1),
    path('link2/', views.link2),
    path('sanpham/<int:id>', views.sanpham),
]
