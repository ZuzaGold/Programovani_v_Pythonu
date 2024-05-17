class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

    def delivery_price(self):
        if self.weight <= 10:
            return 129
        elif self.weight <= 20:
            return 159
        else:
            return 359

class ValuablePackage(Packgage):
    def __init__(self, address, weight, state, value):
        super().__init(address, weight, state)
        self.value = value
    
    def __str__(self):
        return super().__str__() + f" Má hodnotu {self.value} Kč."
    

balik_1 = Package("Václavské náměstí 12, Praha", 0.25, "nedoručen")
print(balik_1)

balik_2 = ValuablePackage("Petrská 113/6, Praha", 15, "doručen", 1500)
print(balik_2)

# # Vytvoření objektů třídy Package
# package1 = Package("Václavské Náměstí 12, Praha", 0.25, "nedoručen")
# package2 = Package("Petrská 113/6, Praha", 15, "doručen")

# # Vypsání informací o balících
# print(package1.get_info())
# print(package2.get_info())

# # Vypsání ceny přepravy pro každý balík
# print(f"Cena přepravy pro první balík je {package1.delivery_price()} Kč.")
# print(f"Cena přepravy pro druhý balík je {package2.delivery_price()} Kč.")


# tak tohle mi taky nefunguje, tak co dělam špatně?????