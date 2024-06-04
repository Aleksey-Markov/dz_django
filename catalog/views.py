from django.shortcuts import render

from catalog.models import Product


def base(request):
    return render(request, 'base.html')


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'home.html', context)


def contacts(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'contacts.html', context)


def products(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product,
        'short_description': product.description[0:100],
        'title': product.title.capitalize
    }
    return render(request, 'products.html', context)
