class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = float(price)
        self.category = category
        self.in_stock = bool(in_stock)
product1 = Product("Smartphone", 12999.99, "Electronics", True)
product2 = Product("Headphones", 499.50, "Accessories", False)
print(product1.name, "-", product1.price, "som")
print(product2.name, "-", product2.price, "som")