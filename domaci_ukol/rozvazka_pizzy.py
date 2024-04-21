class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Pizza {self.name}: stojí {self.price} Kč."

class Pizza(Item):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price)
        self.ingredients = ingredients

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        self.ingredient = ingredient
        self.quantity = quantity
        self.price += quantity * price_per_ingredient
          
Pizza = {
    "Margarita", 200,
    "Prosciuto", 180,
    "Salami", 190
}

ingredients = {
    "sýr": 50,
    "rajčata": 50,
    "olivy": 50,
    "šunka": 50,
    "salám": 50
}

price_per_ingredient = price * 0.1

objednavka = Pizza("Margarita", 200, "olivy")
print(objednavka)



