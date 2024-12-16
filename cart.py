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

    def moyenne(self):
        return (self.calculate_total() / sum(quantity for product, quantity in self.items.items()))
    

    def quantite(self):
    # Demande à l'utilisateur quel produit modifier et la nouvelle quantité
    product_name = input("Quel produit voulez-vous modifier ? ").strip()
    for product in self.items.items():
        if product.name.lower() == product_name.lower():
            new_quantity = int(input(f"Quelle quantité pour {product.name} ? "))
            if new_quantity <= 0:
                # Si la quantité est <= 0, supprime le produit
                self.remove_product(product)
                print(f"{product.name} a été retiré du panier.")
            elif new_quantity > product.stock:
                # Vérifie que la quantité demandée ne dépasse pas le stock disponible
                print(f"Impossible d'ajouter {new_quantity} pour {product.name}. Stock disponible : {product.stock}.")
            else:
                self.items[product] = new_quantity
                print(f"La quantité de {product.name} a été mise à jour à {new_quantity}.")
            return
    print(f"{product_name} n'est pas dans le panier.")
