from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    Model = Product

    def get_queryset(self):
        return Product.objects.order_by('id')


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

# def contacts(request):
#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     message = request.POST.get('message')
#
#     context = {
#         'title': 'Контакты'
#     }
#
#     return render(request, 'catalog/contacts.html', context)


class ProductDetailView(DetailView):
    model = Product
