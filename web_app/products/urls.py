from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('products/', views.prod_view, name='prod'),
    path('customer/<str:pk_test>/', views.customer, name='cust'),
    path('create_order/',views.createOrder,name='create_order'),
]
