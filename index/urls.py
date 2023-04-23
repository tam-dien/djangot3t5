from django.urls import path
from index import views

urlpatterns = [
    # path('', views.index),
    # path('xulytime/', views.xulytime),
    # path('link1/', views.link1),
    # path('link2/', views.link2),
    # path('sanpham/<int:id>', views.sanpham),
    # path('danhsachsanpham/0', views.danhsachsanpham0),
    # path('danhsachsanpham/<int:id>', views.danhsachsanpham),
    # # path('sanpham/<int:id_group>/<int:it_product>', views.dssanpham),
    # path('sanpham/<int:id_group>/<int:id_product>', views.findProduct),
    # path('test_request/', views.testRequest),
    # path('http_method/', views.http_method),
    # path('search_product/', views.search_product),
    # path('login/', views.login),
    # path('add_product/<int:id_group>', views.add_product),
    # path('add_product2/', views.add_product2),
    # path('add_group_product2/', views.add_group_product2),
    # path('product/<int:id>', views.product),
    # path('group/<int:id>', views.group),
    # path('list_group/', views.list_group),
    path('list_product/', views.list_product),
    path('edit_product/<int:id>', views.edit_product),
    # path('delete_product/<int:id>', views.delete_product),
]
