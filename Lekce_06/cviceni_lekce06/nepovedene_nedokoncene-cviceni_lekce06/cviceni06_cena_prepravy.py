class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self._state = state

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self._state}."

    @property
    def delivery_price(self):
        if self.weight <= 10:
            return 129
        elif self.weight <= 20:
            return 159
        else:
            return 359

    def deliver(self):
        if self._state == "doručen":
            return "Balík již byl doručen"
        else:
            self._state = "doručen"
            return "Právě jsem doručil balík"
        

class ValuablePackage(Package):
    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value

    def __str__(self):
        return super().__str__() + f" Má hodnotu {self.value} Kč"
    
    @proprerty
    def _insurance_fee(self):
        return self.value * 0.05
    
    def delivery_price(self):
        return super().delivery_price + self.insurance_fee

balik_1 = Package("Česká 12, Brno", 25.4, "nedoručen")
print(balik_1)

balik_2 = ValuablePackage("Tyršova 11, Praha", 2, "nedoručen", 1500)
print(balik_2)

balik_2.deliver()
print(balik_2)


#  pořád mi to nefunguje, nevim co dělam špatně, zopakovat a přepsat / opravit