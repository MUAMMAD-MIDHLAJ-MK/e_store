from django.shortcuts import render
from .models import Product
from .models import categories

def product_list(request):
    products = Product.objects.all()
  
    
    
    return render(request,
        "product.html",
       
    {"products": products}
    )
    
def categories_list(request):
    category = categories.objects.all()
    
    return render(request, 'category.html',
                  {"category" : category} )