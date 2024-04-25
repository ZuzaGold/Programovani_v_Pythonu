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
        self.ingredients[ingredient] = quantity
        self.price += quantity * price_per_ingredient
        priece_per_ingredient = 0.2

    def __str__(self):
        return f"Pizza {self.name} s extra ingrediencí {self.ingredients} stojí {self.price} Kč."

pizza = {                   # Název, cena
    "Margarita", 200,
    "Prosciuto", 180,
    "Salami", 190
}

ingredients = {             # Název extra ingredience, množství
    "sýr": 50,
    "rajčata": 50,
    "olivy": 50,
    "šunka": 50,
    "salám": 50
}


class Drink(Item):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume
    
    def __str__(self):
        return f"Nápoj {self.name} o objemu {self.volume} ml stojí {self.price} Kč."     

drink = {                   # Název nápoje, množství v ml
    "cola": 500,
    "soda": 500,
    "sprite": 500,
    "mirinda": 500
}

class Order:
    def __init__(self, customer_name, delivery_address, items):
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.items = items
        self.status = "Nová"
    
    def mark_delivered(self):
        self.status = "Doručeno"

    def __str__(self):
        return f"Zákazník {self.custormer_name} s adresou {self.delivery_address} objednal: {self.items}, objednávka {self.status}."

# order_1 = Order("Jaroslav Novák", "Palackého 233, Klatovy", "Margarita", "sýr", "soda")
# order_2 = Order("paní Krásná", "Záletná 20, Lhotka", "Prosciuto", "olivy", "cola")
# order_3 = Order("pan Nerd", "V Koncích 1, Hůrka", "Salami", "mirinda")

order = (
    ["Jaroslav Novák", "Palackého 233, Klatovy", "Margarita", "sýr", "soda"],
    ["paní Krásná", "Záletná 20, Lhotka", "Prosciuto", "olivy", "cola"],
    ["pan Nerd", "V Koncích 1, Hůrka", "Salami", "mirinda"]
)

class DeliveryPerson:
    def __init__(self, name_person, phone_number):
        self.name_person = name_person
        self.phone_number = phone_number
        self.available = True
        self.current_order = None
    
    def assign_order(self, order):
        if self.available:
            self.current_order = order
            # self.current_order.status = "Na cestě"
            return f"Objednávka {self.current_order} byla přiřazena doručovateli {self.name_person} s telefonem {self.phone_number}."
        else:
            self.available = False
            return f"Bohužel momentálně není doručovatel k dispozici."

    def complete_delivery(self):
        if self.current_order:
            self.current_order.mark_delivered()
            return f"Objednávka byla přiřazena doručovateli {self.name_person}, telefonní číslo {self.phone_number}."
            # self.current_order = None
            # self.available = True
    
    def __str__(self):
            return f"Doručovatel {self.name_person} nemá žádnou objednávku k doručení."
        
   
deliveryPerson = (                  # Jméno doručovatele, telefon
    ["Orlando", 775432234],
    ["George", 774123345],
    ["Brandon", 775123321]
)

#kontrola kódu:
# vytvoření objendávky pizzy
print(order[0])
# vytvoření instance doručovatele
deliveryPerson = DeliveryPerson("George", "774123345")
deliveryPerson.assing_order(order[0])
# přiřazení objednávky doručovateli

# doručení objednávky
