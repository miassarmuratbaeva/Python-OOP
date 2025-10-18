class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = float(price)
        self.category = category
        self.in_stock = bool(in_stock)
    def check_stock(self):
        if self.in_stock:
            print(f"{self.name} omborda mavjud ")
        else:
            print(f"{self.name} hozirda tugagan")
product1 = Product("AirPods", 199.99, "Electronics", True)
product2 = Product("iPhone 13", 999.99, "Smartphones", False)
product1.check_stock()
product2.check_stock()