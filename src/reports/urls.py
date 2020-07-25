from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='home'),
    path('product/', views.product_list, name='product_list'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customer/<str:customer_pk>', views.customer_detail, name='customer_detail'),
    path('create_order/', views.create_order, name='create_order'),
    path('update_order/<str:order_pk>', views.update_order, name='update_order'),
    path('delete_order/<str:order_pk>', views.delete_order, name='delete_order'),
    path('location/', views.location, name="location"),
]