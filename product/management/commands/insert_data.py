import requests
from django.utils.text import slugify
from django.core.management import BaseCommand
from product.models import Category,Product
class Command(BaseCommand):
    def handle(self,*args, **options):
        response=requests.get("https://fakestoreapi.com/products").json()
        for object in response:
            category,_=Category.objects.get_or_create(
                title=object['category'],
                slug=slugify(object['category'])
            )
            Product.objects.create(
                category=category,
                title=object['title'],
                slug=slugify(object['title']),
                price=object['price'],
                thumbnail=object['image'],
                description=object['description'],
                
                
            )
        print("Complete")
        