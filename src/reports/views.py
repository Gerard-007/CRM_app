from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views import generic
from django.forms import inlineformset_factory
from .models import Customer, Product, Order
from .forms import CreateOrderForm

# Create your views here.

def report_list(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    open_orders = orders.filter(status="Out for delivery").count()
    orders_delivered = orders.filter(status="Delivered").count()
    orders_pending = orders.filter(status="Pending").count()
    context = {'orders': orders, 
                'customers': customers,
                'total_customers': total_customers,
                'total_orders': total_orders,
                'orders_delivered': orders_delivered,
                'orders_pending': orders_pending,
                'open_orders': open_orders
            }
    return render(request, "reports/dashboard.html", context)

def product_list(request):
    products = Product.objects.all()
    return render(request, "reports/product_list.html", {'products': products})

def customer_list(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, "reports/customer_list.html", context)

def customer_detail(request, customer_pk):
    customer = get_object_or_404(Customer, id=customer_pk)
    customer_orders = customer.order_set.all()
    customer_orders_count = customer_orders.count()
    context = {'customer': customer, 'customer_orders': customer_orders, 'customer_orders_count': customer_orders_count}
    return render(request, "reports/customer_detail.html", context)


def create_order(request, customer_pk):
    order_form_set = inlineformset_factory(Customer, Order, fields=('product', 'quantity', 'status'))
    customer = get_object_or_404(Customer, id=customer_pk)
    form_set = order_form_set(instance=customer)
    # form = CreateOrderForm(initial={'customer':customer})
    if request.method == "POST":
        # print(f"posting-{request.POST}")
        form = CreateOrderForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form_set': form_set}
    return render(request, "reports/order_form.html", context)


# def create_order(request):
#     form = CreateOrderForm()
#     if request.method == "POST":
#         # print(f"posting-{request.POST}")
#         form = CreateOrderForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('home')
#     context = {'form': form}
#     return render(request, "reports/order_form.html", context)


def update_order(request, order_pk):
    order = get_object_or_404(Order, id=order_pk)
    form = CreateOrderForm(instance=order)
    if request.method == "POST":
        # print(f"posting-{request.POST}")
        form = CreateOrderForm(request.POST, instance=order)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, "reports/order_form.html", context)


def delete_order(request, order_pk):
    order = get_object_or_404(Order, id=order_pk)
    if request.method == "POST":
        order.delete()
        return redirect('home')
    context = {'item': order}
    return render(request, "reports/delete.html", context)


def location(request):
    mapbox_access_token = 'pk.eyJ1IjoiZ2VldGVjaCIsImEiOiJjazNieTMwZGgwN2p6M21vMnBsMG1ldDd4In0.M162n_OVG3VT8hlN9Uw93g'
    return render(request, 'reports/location.html', {"mapbox_access_token": mapbox_access_token})

# class ReportList(generic.ListView):
#     template_name = "reports/dashboard.html"
