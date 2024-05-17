class Package:
    def __init__(self, address, weight, state="nedoručen"):
        self.address = address
        self.weight = weight
        self._state = state  # Chráněný atribut

class ValuablePackage(Package):
    def __init__(self, address, weight, state="nedoručen", value):
        super().__init__(address, weight, state="nedoručen")
        self.value = value
    
    def __str__(self):
        return super().__str__ + ". " + "Má hodnotu 1000 EUR."

    def __str__(self):
        return f"Balík na adresu {self.address}, váha {self.weight} kg, je ve stavu {self._state}."
        
    def deliver(self):
        if self._state == "doručen":
            return "Balík již byl doručen."
        else:
            self._state = "doručen"
            return "Doručení uloženo."

# Vytvoření a testování objektů třídy Package
package1 = Package("Václavské náměstí 12, Praha", 0.5, 1000)
package2 = Package("Příkopy 23, Brno", 1.2)

print(package1)
print(package2)

# Testování doručení
print(package1.deliver())
print(package1.deliver())  # Zkusíme doručit znovu

print(package2.deliver())


# pořád mi to nefunguje, musim to opravit