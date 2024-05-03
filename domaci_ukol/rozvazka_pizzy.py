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
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = quantity
            self.price += quantity * price_per_ingredient        
        else:
            print(f"Ingredience navíc {self.ingredient} není k dispozici")

    def __str__(self):
        ingredients_str = ", ".join([f"{ingredient} ({quantity} g)" for ingredient, quantity in self.ingredients.items()]) 
        return f"Pizza {self.name} - Ingredience: {ingredients_str}, stojí celkem {self.price} Kč."

    # def __str__(self):
    #     return f"Pizza {self.name} s ingrediencí {self.ingredient} stojí celkem {self.price} Kč."

# Název, cena, ingredience
margarita = Pizza("Margarita", 180, {"sýr": 100, "rajčata": 150})
prosciuto = Pizza("Prosciuto", 195, {"sýr": 100, "rajčata": 150, "šunka": 150, "jalapenos": 150})
salami = Pizza("Salami", 190, {"sýr": 100, "rajčata": 150, "salám": 100})
spinaci = Pizza("Spinaci", 210, {"sýr": 100, "smetana": 100, "špenát": 100, "olivy": 150})

ingredients = {
            "sýr": (100, 1),
            "rajčata": (150, 1),
            "šunka": (150, 1),
            "salám": (100, 1),
            "špenát": (100, 1),
            "smetana": (100, 1),
            "olivy": (100, 0.25),
            "jalapenos": (100, 0.25),
            "houby": (100, 0.25)
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


class Order:
    def __init__(self, customer_name, delivery_address, items):
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.items = items
        self.status = "Nová objednávka"
    
    def mark_delivered(self):
        self.status = "Objednávka doručena"

    def __str__(self):
        item_list = "/".join([str(item) for item in self.items])
        return f"{self.status}: {self.customer_name} / {self.delivery_address} / {item_list}."
    
Jaroslav_Novak = Order("Jaroslav Novák", "Palackého 233, Klatovy", ["Pizza Spinaci", {"olivy": 100}])
pani_Krasna = Order("paní Krásná", "Záletná 20, Lhotka", ["Pizza Prosciuto", {"jalapenos": 100}, "cola"])
pan_Nerd = Order("pan Nerd", "V Koncích 1, Hůrka", ["Pizza Salami", "soda"])


class DeliveryPerson:
    def __init__(self, name_person, phone_number):
        self.name_person = name_person
        self.phone_number = phone_number
        self.available = True
        self.current_order = None
    
    def assign_order(self, order):
        if self.available:
            if self.current_order is None:
                self.current_order = order
                self.current_order.status = "Objednávka na cestě"
                return f"{self.current_order.status} / byla přiřazena doručovateli {self.name_person} {self.phone_number}."
            else:
                self.available = False
                return f"Doručovatel {self.name_person} už má přiřazenou objednávku a není k dispozici."
        else: 
            return f"Doručovatel {self.name_person} není k dispozici."


    def complete_delivery(self):
        if self.current_order:
            self.current_order.mark_delivered()
            self.current_order = None
            self.available = True
            return f"Objednávka byla doručena doručovatelem {self.name_person}, telefonní číslo {self.phone_number}." 
    
    def __str__(self):
            availability = "available" if self.available else "not available"
            return f"Doručovatel {self.name_person} je volný."
        
   
# Jméno doručovatele, telefon
orlando = DeliveryPerson("Orlando", 775432234)
george = DeliveryPerson("George", 774123345)
brandon = DeliveryPerson("Brandon", 775123321)


#kontrola kódu:
order = Jaroslav_Novak
print(Jaroslav_Novak)
deliveryPerson = george
print(george)
print(george.assign_order(Jaroslav_Novak))
# Doručovatel George teď není k dispozici.
print(george.assign_order(Jaroslav_Novak))

order = pani_Krasna
print(pani_Krasna)
print(george.assign_order(pani_Krasna))   # kontrola, jestli George opravdu není k dispozici
deliveryPerson = orlando
print(orlando)
print(orlando.assign_order(pani_Krasna))
print(deliveryPerson.complete_delivery())
print(pani_Krasna.mark_delivered())


order = pan_Nerd
print(pan_Nerd)
print(george.assign_order(pan_Nerd))
print(orlando.assign_order(pan_Nerd))

