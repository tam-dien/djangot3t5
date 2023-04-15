from django.urls import path
from index import views

urlpatterns = [
    path('', views.index),
    path('xulytime/', views.xulytime),
    path('link1/', views.link1),
    path('link2/', views.link2),
    path('add_product/', views.add_product),
    path('product/<int:id>', views.product),
    path('list_product/', views.list_product),
    path('edit_product/<int:id>', views.edit_product),
    path('delete_product/<int:id>', views.delete_product),

]
