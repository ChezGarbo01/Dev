import requests
import urllib.parse

def geocoding(location, key):
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q": location, "limit": "1", "key": key})

    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code
    print("Geocoding API URL for " + location + ":\n" + url)

    if json_status == 200:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
    else:
        lat = "null"
        lng = "null"
    return json_status, lat, lng

# Replace with your API key
key = "12abf47a-8b26-4187-803a-3e0995fc5634"

# POS System with Products and Features
class POS:
    def __init__(self):
        self.products = []

    def add_product(self, product_name, price, quantity):
        product = {
            "name": product_name,
            "price": price,
            "quantity": quantity,
            "subtotal": price * quantity
        }
        self.products.append(product)

    def list_products(self):
        print("\nCurrent Products in Cart:")
        for idx, product in enumerate(self.products, start=1):
            print(f"{idx}. {product['name']} - ₱{product['price']:.2f} x {product['quantity']} = ₱{product['subtotal']:.2f}")

    def calculate_total(self):
        total = sum(product["subtotal"] for product in self.products)
        return total

    def checkout(self):
        self.list_products()
        total = self.calculate_total()
        print(f"\nTotal Amount: ₱{total:.2f}")

# Sample Usage of POS System
pos = POS()

# Add 5 sample products
pos.add_product("Rolex", 750000.00, 1)  # Price of a Rolex watch
pos.add_product("Shirt", 500.00, 3)     # Price per shirt
pos.add_product("Shorts", 800.00, 2)    # Price per pair of shorts
pos.add_product("Shoes", 3500.00, 1)    # Price per pair of shoes
pos.add_product("Pants", 1200.00, 2)    # Price per pair of pants

# List products and checkout
pos.list_products()
pos.checkout()

# Optional: Add geocoding for store locations
loc1 = "Angeles City, Philippines"
loc2 = "Mabalacat City, Philippines"
loc3 = "Tarlac City, Philippines"
loc4 = "Baguio, Philippines"
loc5 = "Nueva Ecija, Philippines"

orig = geocoding(loc1, key)
dest = geocoding(loc2, key)
tarlac = geocoding(loc3, key)
baguio = geocoding(loc4, key)
nueva_ecija = geocoding(loc5, key)

print(f"\nStore Location 1: {orig}")
print(f"Store Location 2: {dest}")
print(f"Store Location 3 (Tarlac): {tarlac}")
print(f"Store Location 4 (Baguio): {baguio}")
print(f"Store Location 5 (Nueva Ecija): {nueva_ecija}")
