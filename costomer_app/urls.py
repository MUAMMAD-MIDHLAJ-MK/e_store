from django.urls import path
from .views import register_costomer
from django.conf.urls.static import static

app_name = 'costomer_app'

urlpatterns = [
  path('', register_costomer, name='register')
    
]
