import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from db.models import Product

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import Product

def populate_products():
    products = [
        {"upc": "123456789012", "name": "Apple", "price": 0.99},
        {"upc": "987654321098", "name": "Banana", "price": 0.69},
        {"upc": "456789123456", "name": "Orange Juice", "price": 3.49},
        {"upc": "654321987654", "name": "Bread", "price": 2.99},
    ]
    for p in products:
        Product.objects.get_or_create(
            upc=p["upc"],
            defaults={"name": p["name"], "price": p["price"]}
        )

def scan_product():
    upc_input = input("Enter UPC code: ").strip()
    try:
        product = Product.objects.get(upc=upc_input)
        print(f"Product: {product.name}\nPrice: ${product.price}")
    except Product.DoesNotExist:
        print("Product not found!")

if __name__ == "__main__":
    populate_products()
    print("Database populated with sample products.")
    while True:
        scan_product()
