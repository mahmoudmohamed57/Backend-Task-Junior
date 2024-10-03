from django.core.management.base import BaseCommand
from ...models import Category, Subcategory, Product

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Subcategory.objects.all().delete()
        Product.objects.all().delete()

        electronics = Category.objects.create(name='Electronics')
        clothing = Category.objects.create(name='Clothing')
        home_appliances = Category.objects.create(name='Home Appliances')

        mobile_phones = Subcategory.objects.create(name='Mobile Phones', category=electronics)
        laptops = Subcategory.objects.create(name='Laptops', category=electronics)
        men_clothing = Subcategory.objects.create(name='Men Clothing', category=clothing)
        women_clothing = Subcategory.objects.create(name='Women Clothing', category=clothing)
        kitchen_appliances = Subcategory.objects.create(name='Kitchen Appliances', category=home_appliances)

        Product.objects.create(name='iPhone 14', description='Latest model of iPhone', subcategory=mobile_phones)
        Product.objects.create(name='Samsung Galaxy S21', description='High-end smartphone', subcategory=mobile_phones)
        Product.objects.create(name='Dell XPS 13', description='Powerful and portable laptop', subcategory=laptops)
        Product.objects.create(name='Men T-Shirt', description='Comfortable cotton t-shirt', subcategory=men_clothing)
        Product.objects.create(name='Women Dress', description='Stylish summer dress', subcategory=women_clothing)
        Product.objects.create(name='Blender', description='High-speed blender for smoothies', subcategory=kitchen_appliances)

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
