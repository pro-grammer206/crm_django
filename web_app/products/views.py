from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import OrderForm

# Create your views here.
app_name = 'products'
posts = [{'name': 'Vipin',
          'blog_post': 'This is a sample blog post regarding post',
          'pub_date': '20/06/2020'},
         {'name': 'John',
          'blog_post': 'This is a sample blog post regarding post',
          'pub_date': '20/06/2020'}
         ]


def home_view(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()

    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered, 'pending': pending}
    return render(request, 'products/dashboard.html', context)


def prod_view(request):
    products = Product.objects.all()

    return render(request, 'products/prod.html', {'products': products})


def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'products/customer.html', context)


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'products/order_form.html',context)


