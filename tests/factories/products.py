import factory
from factory.django import DjangoModelFactory

from core.apps.products.models.products import Product


class ProductModelFactory(DjangoModelFactory):
    title = factory.Faker('first_name')
    description = factory.Faker('text')

    class Meta:
        model = Product
