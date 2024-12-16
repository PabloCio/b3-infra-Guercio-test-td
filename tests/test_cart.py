import unittest
from cart import Cart
from product import Product

class TestCart(unittest.TestCase):

    def __init__(self, name: str, price: float, mtc: int):
        self.name = name
        self.price = price
        self.mtc = mtc

    p1 = Product("Laptop", 1000, 5)
    p2 = Product("Headphones", 50, 20)
    p3 = Product("Mouse", 25, 10)

    cart = Cart()

    cart.add_product(p1, 2)  #(2 * 1000 = 2000€)
    cart.add_product(p2, 4)  #(4 * 50 = 200€)
    cart.add_product(p3, 5)  #(5 * 25 = 125€)
    cart.mettre_de_cote(p3)

    # Test de la méthode moyenne
    print("[Test] Testing Moyenne...")
    moyenne = 211,36363636363636363636363636364
    if moyenne == cart.moyenne():
        print("[Test] Product passed.")
    else :
        print("[Test] Product not passed.")

    # Test de la méthode quantite (total des quantités dans le panier)
    print("[Test] Testing quantité...")
    total_quantite = cart.quantite()
    print(f"Quantité totale de produits dans le panier : {total_quantite}")

    # Test de la fonction mettre_de_cote
    print("[Test] Testing mettre de cote...")
    quantity = 6
    if quantity == cart.quantite()
        print("[Test] Product passed.")
    else :
        print("[Test] Product not passed.")