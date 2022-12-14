from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.header, name='header'),
    path("products/", views.products, name="products"),
    path('create-card/', views.create_card, name='create-card'),
    path('update-card/<str:pk>', views.update_card, name='update-card'),
    path('delete-card/<str:pk>', views.delete_card, name='delete-card'),
    path('product-card/<str:pk>', views.product_card, name='product-card'),
    
    path('order/', views.order, name='order'),
    path('add-orderItem/<str:pk>', views.add_orderItem, name='add-orderItem'),
    path('update-orderItem/<str:pk>', views.update_orderItem, name='update-orderItem'),
    path('delete-orderItem/<str:pk>', views.delete_orderItem, name='delete-orderItem'),
    path('checkout/<str:pk>', views.chekout, name='checkout'),
    path('add-shippingAddress/', views.add_ShippingAddress, name='add-shippingAddress'),
    path('update_shippingaddress/<str:pk>', views.update_ShippingAddress, name='update_shippingAddress'),
]