from django.shortcuts import render
from orders.models import Order
from products.models import Product

def sales_analytics(request):
    total_orders = Order.objects.count()
    total_products = Product.objects.count()
    return render(request, 'dashboard/analytics.html', {
        'total_orders': total_orders,
        'total_products': total_products
    })
