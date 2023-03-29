from django.urls import path
from index import views

urlpatterns = [
    path('', views.index),
    path('xulytime/', views.xulytime),
    path('link1/', views.link1),
    path('link2/', views.link2),
    path('sanpham/<int:id>', views.sanpham),
    path('danhsachsanpham/0', views.danhsachsanpham0),
    path('danhsachsanpham/<int:id>', views.danhsachsanpham),
    # path('sanpham/<int:id_group>/<int:it_product>', views.dssanpham),
    path('sanpham/<int:id_group>/<int:id_product>', views.findProduct),
    path('test_request/', views.testRequest),
    path('http_method/', views.http_method),
    path('search_product/', views.search_product),
    path('login/', views.login),
    path('add_product/<int:id_group>', views.add_product),
]
