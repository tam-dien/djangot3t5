from django.urls import path
from index import views

urlpatterns = [
    path('', views.index),
    path('xulytime/', views.xulytime),
    path('link1/', views.link1),
    path('link2/', views.link2),
    path('sanpham/<int:id>', views.sanpham),
    path('dssanpham/<int:id>', views.danhsachsanpham),
    path('sanpham2/<int:id_group>/<int:id_product>',views.sanpham2)
]
