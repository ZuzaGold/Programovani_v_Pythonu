class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Položka {self.name}: stojí {self.price} Kč."

class Pizza(Item):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price)
        self.ingredients = ingredients

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        if ingredient in self.ingredient_prices:
            self.ingredient = ingredient
            self.quantity = quantity
            self.price_per_ingredient = price_per_ingredient
            self.ingredients[ingredient] = quantity
            self.price += quantity * price_per_ingredient        
        else:
            print(f"Ingredience navíc {self.ingredient_prices} není k dispozici")

    # def __str__(self):
    #     ingredients_str = ", ".join([f"{ingredient} ({quantity} g)" for ingredient, quantity in self.ingredients.items()]) 
    #     return f"Pizza {self.name} - Ingredience: {ingredients_str}, stojí celkem {self.price} Kč."

    def __str__(self):
        return f"Pizza {self.name} s ingrediencí {self.ingredient} stojí celkem {self.price} Kč."

# Název, cena, ingredience
margarita = Pizza("Margarita", 180, {"sýr": 100, "rajčata": 150})
prosciuto = Pizza("Prosciuto", 195, {"sýr": 100, "rajčata": 150, "šunka": 150})
salami = Pizza("Salami", 190, {"sýr": 100, "rajčata": 150, "salám": 150})
spinaci = Pizza("Spinaci", 210, {"sýr": 100, "smetana": 100, "špenát": 150})

ingredient_prices = {
            "sýr": (1, 0.2),
            "rajčata": (1, 0.15),
            "šunka": (1, 0.2),
            "salám": (1, 0.15),
            "špenát": (1, 0.2),
            "smetana": (1, 0.25)
            }

class Drink(Item):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume

    def __str__(self):
        return f"Nápoj {self.name} {self.volume} ml stojí {self.price} Kč."     

# Název nápoje, množství v ml
cola = Drink("cola", 45, 500)
soda = Drink("soda", 25, 500)
mirinda = Drink("mirinda", 45, 500)

# def calculate_order_price(pizza, drink, ingredient_prices):
#     for ingredient in ingredient_prices:
#         cena_celkem = Pizza.price + Drink.price + price_per_ingredient
#         return cena_celkem

# def calculate_order_price(pizza, drink):
#     total_price = pizza.price + drink.price
#     return total_price

# def __str__(self):
#     total_price = calculate_order_price(self.pizza.price, self.drink.price)
#     return f"Celková cena objednávky: {total_price} Kč."

class Order:
    def __init__(self, customer_name, delivery_address, items):
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.items = items
        self.status = "Nová objednávka"
    
    def mark_delivered(self):
        self.status = "Doručeno"

    def __str__(self):
        item_list = "/".join([str(item) for item in self.items])
        return f"{self.status}: {self.customer_name} / {self.delivery_address} / {self.items}."

Jaroslav_Novak = Order("Jaroslav Novák", "Palackého 233, Klatovy", ["Pizza Spinaci", {"špenát": 50}])
pani_Krasna = Order("paní Krásná", "Záletná 20, Lhotka", ["Pizza Prosciuto", {"špenát": 50}, "cola"])
pan_Nerd = Order("pan Nerd", "V Koncích 1, Hůrka", ["Pizza Salami", "soda"])


class DeliveryPerson:
    def __init__(self, name_person, phone_number):
        self.name_person = name_person
        self.phone_number = phone_number
        self.available = True
        self.current_order = None
    
    def assign_order(self, order):
        if self.available:
            self.current_order = order
            self.current_order.status = "Objednávka na cestě"
            return f"{self.current_order.status} / byla přiřazena doručovateli." # byla přiřazena doručovateli {self.name_person} s telefonem {self.phone_number}."
        else:
            self.available = False
            return f"Bohužel momentálně není doručovatel k dispozici."

    def complete_delivery(self):
        if self.current_order:
            self.current_order.mark_delivered()
            self.current_order = None
            self.available = True
            return f"Objednávka byla doručena doručovatelem {self.name_person}, telefonní číslo {self.phone_number}." 
    
    def __str__(self):
            availability = "available" if self.available else "not available"
            return f"Doručovatel {self.name_person} nemá žádnou objednávku k doručení."
        
   
# Jméno doručovatele, telefon
Orlando = DeliveryPerson("Orlando", 775432234)
George = DeliveryPerson("George", 774123345)
Brandon = DeliveryPerson("Brandon", 775123321)


# #kontrola kódu:
# # vytvoření nové objendávky pizzy
# Order = Jaroslav_Novak
# print(Jaroslav_Novak)
# # vytvoření instance volného doručovatele
# DeliveryPerson = George
# # přiřazení objednávky doručovateli
# print(DeliveryPerson.assign_order(Jaroslav_Novak))
# print(George)
# # doručení objednávky
# print(DeliveryPerson.complete_delivery())
# print(Order)


Order = pani_Krasna
print(pani_Krasna)
DeliveryPerson = Orlando
print(DeliveryPerson.assign_order(pani_Krasna))
print(Orlando)
print(DeliveryPerson.complete_delivery())
print(Order)
print(Pizza.price)

