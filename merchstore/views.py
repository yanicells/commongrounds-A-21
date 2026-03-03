from django.shortcuts import render

from .models import Product


def item_list(request):
    products = Product.objects.all()
    ctx = {
        'products': products
    }
    return render(request, 'merchstore/item_list.html', ctx)


def item_detail(request, pk):
    product = Product.objects.get(pk=pk)
    ctx = {
        'product': product
    }
    return render(request, 'merchstore/item_detail.html', ctx)
