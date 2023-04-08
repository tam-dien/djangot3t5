from django.urls import path
from index import views

urlpatterns = [
    path('', views.index),
    path('xulytime/', views.xulytime),
    path('link1/', views.link1),
    path('link2/', views.link2),
    path('sanpham/<int:id>/',views.sanpham),
    path('danhsachsanpham/0/',views.danhsachsanpham0),
    path('danhsachsanpham/<int:id>/',views.danhsachsanpham),
    path('sanpham2/<int:id_group>/<int:id_product>/',views.sanpham2),
    path('testrequest/',views.testrequest),
    path('searchproduct/', views.searchproduct),
    path('login/', views.login),
    path('addproduct/', views.addproduct),
    path('product/<int:idproduct>/', views.product),
    path('listproduct/', views.list_product),
    path('editproduct/<int:id>/', views.editproduct),
    path('deleteproduct/<int:id>/', views.deleteproduct),
]
