import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read():
        with open('data.json', 'r', encoding='utf8') as file:
            data = json.load(file)
            return data

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read():
            if category['model'] == 'catalog.category':
                category_for_create.append(Category(title=category['fields']['title'],
                                                    description=category['fields']['description']))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read():
            if product['model'] == 'catalog.product':
                product_for_create.append(Product(title=product['fields']['title'],
                    description=product['fields']['description'],
                    category_name=Category.objects.get(pk=product['fields']['category_name'],
                    image=product['fields']['image'], price=product['fields']['price'],
                    created_at=product['fields']['created_at'], updated_at=product['fields']['updated_at'])))

        Product.objects.bulk_create(product_for_create)