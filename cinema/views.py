from django.shortcuts import render
from products.models import *




def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_serials = products_images.filter(product__category__id=1)
    products_images_films = products_images.filter(product__category__id=2)
    return render(request, 'main.html', locals())