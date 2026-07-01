from django.shortcuts import render, get_object_or_404
from .models import Category


def category_products(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.products_set.all()

    return render(request,  'category_app/category.html', {
        'category': category,
        'products': products,
    })



def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {
        'categories': categories
    })