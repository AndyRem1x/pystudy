class Product:
    def __init__(self, product_type, product_name, product_price):
        self.type = product_type
        self.name = product_name
        self.price = product_price

    def __repr__(self):
        return f"'Name': {self.name}. 'Type': {self.type}. 'Price': {self.price}"


class ProductStore:
    def __init__(self, discount=30):
        self.storage = {}
        self.categories_set = {}
        self.discount = discount
        self.income = 0

    def create_storage_item(self, product, amount):
        if product.type not in self.categories_set:
            self.categories_set[product.type] = set(product.name)
        else:
            self.categories_set[product.type].add(product.name)

        return {
            "product": product,
            "amount": amount,
            "discount": self.discount,
        }

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Invalid type of product")
        if not isinstance(amount, int) or isinstance(amount, float) or amount <= 0:
            raise ValueError("Invalid amount value")
        if product.name not in self.storage:
            self.storage[product.name] = self.create_storage_item(product, amount)
        else:
            self.storage[product.name]["amount"] = (
                self.storage[product.name][product].get("amount", 0) + amount
            )

    def set_discount(self, identifier, percent, identifier_type="name"):
        if not isinstance(identifier, str) or len(identifier) == 0:
            raise ValueError("Invalid identifier value")
        if not isinstance(percent, int):
            raise ValueError("Invalid percent value")
        success = 0
        if identifier_type == "name":
            self.storage[identifier]["discount"] = percent
            success = 1
        else:
            for product_name in self.categories_set[identifier]:
                self.storage[product_name]["discount"] = percent
                success = 1
        if success == 0:
            raise ValueError(f"Product with {identifier_type}: '{identifier}' not found")

    def sell_product(self, product_name, amount):
        if product_name not in self.storage:
            raise ValueError(f"Product with name: '{product_name}' not found")
        if (not isinstance(amount, int) or isinstance(amount, float) or amount <= 0 or self.storage[product_name]["amount"] - amount < 0):
            raise ValueError("Invalid amount value")
        self.storage[product_name]["amount"] -= amount
        self.income = (self.storage[product_name]["product"].price * (1 - self.storage[product_name]["discount"] / 100)* amount)

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.storage

    def get_product_info(self, product_name):
        if product_name not in self.storage:
            raise ValueError(f"Product named: '{product_name}' not found")
        return product_name, self.storage[product_name].get("amount", 0)


product = Product("Clothes", "Hoodie", 400)
product2 = Product("Shoes", "Sneakers", 2500)

store = ProductStore()
store.add(product, 200)
store.add(product2, 500)
print("Products in storage with default discount:", store.get_all_products(), sep="\n")
store.set_discount("Hoodie", 30)
store.sell_product("Hoodie", 150)
print('The amount of products in storage with 30% discount for "Hoodie":', store.get_all_products(), sep="\n")
print('Store income after selling 150 items of "Hoodie":', store.get_income())

assert store.get_product_info("Hoodie") == ("Hoodie", 50)
assert store.get_income() == 42000
