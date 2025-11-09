import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from db.models import Product


def populate_products():
    Product.objects.all().delete()

    Product.objects.create(upc="123456789012", name="Apple", price=0.99)
    Product.objects.create(upc="234567890123", name="Banana", price=0.59)
    Product.objects.create(upc="345678901234", name="Milk", price=2.49)
    Product.objects.create(upc="456789012345", name="Bread", price=1.99)
    Product.objects.create(upc="567890123456", name="Eggs", price=3.49)

    print("✅ Database populated with sample products:")
    for p in Product.objects.all():
        print(f"UPC: {p.upc} | {p.name} - ${p.price}")


def scan_product():
    while True:
        code = input("\nScan product UPC (or type 'exit' to quit): ")
        if code.lower() == "exit":
            print("Exiting program...")
            break

        try:
            product = Product.objects.get(upc=code)
            print(f"🛒 Scanned: {product.name} - ${product.price}")
        except Product.DoesNotExist:
            print("❌ Product not found. Please try again.")


if __name__ == "__main__":
    populate_products()
    scan_product()
