
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from product_app.models import Product



def cart_list(request,product_id=None):

    if product_id:
        carts = Cart.objects.filter(product_id=product_id)
    else:
        carts = Cart.objects.all()

    total = sum(item.total_price() for item in carts)

    return render(request, "cart.html", {
        "carts": carts,
        "total": total
    })


def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart, created = Cart.objects.get_or_create(product=product)

    if not created:
        cart.quantity += 1
        cart.save()

    return redirect("cart:cart_list")


def remove_cart(request, cart_id):

    cart = get_object_or_404(Cart, id=cart_id)

    cart.delete()

    return redirect("cart:cart_list")


def clear_cart(request):

    Cart.objects.all().delete()

    return redirect("cart:cart_list")