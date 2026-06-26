from django.urls import path
from . import views

app_name = "category_app"

urlpatterns = [
     path('', views.category_list, name='category_list'),
     path('<int:id>/', views.category_products, name='category_products'),
]