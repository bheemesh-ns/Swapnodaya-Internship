#multilevel inheritance

class product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price
    def display_product(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price: {self.price}")

class Electronic_product(product):
    def __init__(self, product_name, price, brand, warranty):
        super().__init__(product_name, price)
        self.brand = brand
        self.warranty = warranty
    def display_electronic_product(self):
        print(f"Brand: {self.brand}")
        print(f"Warranty: {self.warranty}")

class Mobile_phone(Electronic_product):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
        super().__init__(product_name, price, brand, warranty)
        self.ram = ram
        self.storage = storage
    def diaplay_mobile_details(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price: {self.price}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")

obj = Mobile_phone("iPhone", 69999, "Apple", "1 year", "8GB", "128GB")
obj.display_product()
obj.display_electronic_product()
obj.diaplay_mobile_details()