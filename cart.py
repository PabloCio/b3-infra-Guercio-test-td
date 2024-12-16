# cart.py

from product import Product

class Cart:
    def __init__(self):
    #initialise la poo sur python 
        self.items = {}  # {product: quantity}

    def add_product(self, product: Product, quantity: int):
    # ajoute un produit
        if product.stock < quantity:
            raise ValueError(f"Cannot add {quantity} of {product.name}. Only {product.stock} left.")
        self.items[product] = self.items.get(product, 0) + quantity

    def remove_product(self, product: Product):
    # supprime le produit
        if product in self.items:
            del self.items[product]
        else:
            raise KeyError(f"{product.name} is not in the cart.")

    def calculate_total(self):
    # calcule le total
        return sum(product.price * quantity for product, quantity in self.items.items())

    def display_cart(self):
    # affiche le panier
        if not self.items:
            return "Your cart is empty."
        return "\n".join([f"{product.name} x {quantity} - {product.price * quantity}€"
                          for product, quantity in self.items.items()])
