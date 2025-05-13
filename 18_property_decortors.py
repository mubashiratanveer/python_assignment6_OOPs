class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        print("Setting price...")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price


# Example usage:
p = Product(100)
print(p.price)     # Getting price... → 100

p.price = 150      # Setting price...
print(p.price)     # Getting price... → 150

del p.price        # Deleting price...
