import unittest
from cart import Cart

class TestCart(unittest.TestCase):

    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.mtc = mtc

    # Tests de la classe Cart
    def test_cart_methods():
    # Crée des produits
    p1 = Product("Laptop", 1000, 5)
    p2 = Product("Headphones", 50, 20)
    p3 = Product("Mouse", 25, 10)

    # Crée un panier
    cart = Cart()

    # Ajoute des produits au panier
    cart.add_product(p1, 2)  # 2 laptops (2 * 1000 = 2000€)
    cart.add_product(p2, 4)  # 4 headphones (4 * 50 = 200€)
    cart.add_product(p3, 5)  # 5 mice (5 * 25 = 125€)

    # Test de la méthode moyenne
    print("[Test] Testing Moyenne...")
    moyenne = 211,36363636363636363636363636364
    if moyenne == cart.moyenne()
    print("[Test] Product passed.")
    else
    print("[Test] Product not passed.")

    # Test de la méthode quantite (total des quantités dans le panier)
      print("[Test] Testing quantité...")
    total_quantite = cart.quantite()
    print(f"Quantité totale de produits dans le panier : {total_quantite}")

    # Test de la fonction mmettre_de_cote
    total_quantite = cart.quantite()
    print(f"Quantité totale de produits dans le panier : {total_quantite}")