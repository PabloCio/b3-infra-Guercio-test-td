from cart import *
# Classe Product (assurez-vous que cela existe dans votre code)
class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

# Tests de la classe Cart
def test_cart_methods():
    # Crée des produits
    product1 = Product("Laptop", 1000, 5)
    product2 = Product("Headphones", 50, 20)
    product3 = Product("Mouse", 25, 10)

    # Crée un panier
    cart = Cart()

    # Ajoute des produits au panier
    cart.add_product(product1, 2)  # 2 laptops (2 * 1000 = 2000€)
    cart.add_product(product2, 4)  # 4 headphones (4 * 50 = 200€)
    cart.add_product(product3, 5)  # 5 mice (5 * 25 = 125€)

    # Test de la méthode moyenne
    moyenne = cart.moyenne()
    print(f"Prix moyen par produit dans le panier : {moyenne:.2f}€")

    # Test de la méthode quantite (total des quantités dans le panier)
    total_quantite = cart.quantite()
    print(f"Quantité totale de produits dans le panier : {total_quantite}")

    # Test de la fonction mmettre_de_cote
    total_quantite = cart.quantite()
    print(f"Quantité totale de produits dans le panier : {total_quantite}")

    # Appeler les tests
    
