from product import Product

class Cart:
    def __init__(self):
        self.items = {}  # {product: quantity}
        self.mtd = {} # {product: quantity}

    def add_product(self, product: Product, quantity: int):
        if product.stock < quantity:
            raise ValueError(f"Cannot add {quantity} of {product.name}. Only {product.stock} left.")
        self.items[product] = self.items.get(product, 0) + quantity

    def remove_product(self, product: Product):
        if product in self.items:
            del self.items[product]
        else:
            raise KeyError(f"{product.name} is not in the cart.")

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def display_cart(self):
        if not self.items:
            return "Your cart is empty."
        return "\n".join([f"{product.name} x {quantity} - {product.price * quantity}€"
                          for product, quantity in self.items.items()])

    def moyenne(self):
        return self.calculate_total() / sum(quantity for product, quantity in self.items.items())

    def quantite(self):
        product_name = input("Quel produit voulez-vous modifier ? ").strip()
        for product in self.items.keys():
            if product.name.lower() == product_name.lower():
                try:
                    new_quantity = int(input(f"Quelle quantité pour {product.name} ? "))
                except ValueError:
                    print("Veuillez entrer un nombre valide.")
                    return

                if new_quantity <= 0:
                    self.remove_product(product)
                    print(f"{product.name} a été retiré du panier.")
                elif new_quantity > product.stock:
                    print(f"Impossible d'ajouter {new_quantity} pour {product.name}. Stock disponible : {product.stock}.")
                else:
                    self.items[product] = new_quantity
                    print(f"La quantité de {product.name} a été mise à jour à {new_quantity}.")
                return
        print(f"{product_name} n'est pas dans le panier.")

    def mettre_de_cote(self, product: Product, quantity: int):
        product_name = input("Quel produit voulez-vous mettre de coter ? ").strip()
        if product_name in self.items:
            quantity = self.items[product]
            self.mtd[product] = self.mtd.get(product, 0) + quantity
            del self.items[product]
        else:
            print(f"{product.name} n'est pas dans le panier.")
        raise KeyError(f"{product.name} is not in the cart.")