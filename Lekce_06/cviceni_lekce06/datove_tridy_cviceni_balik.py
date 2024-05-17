from dataclasses import dataclass

@dataclass
class Package:
    address: set
    weight: float
    state: str

    def __str__(self):
        return f"balík na adresu: {self.address}, Váha: {self.weight} kg, Stav: {self.state}"

def delivery_price(self):
    if self.weight <= 10:
        return 129
    elif self.weight <= 20:
        return 159
    else:
        return 359

package = Package("Grimmauldovo náměstí 11", 15, "nedoručen")
print(package)

@dataclass
class ValuablePackage(Package):
    value: int

    def __str__(self):
        return super().__str__() + F", Hodnota balíku: {self.value} Kč."
    
valuable_package = ValuablePackage("Godrikův důl 47", 3, "nedoručen", 20000)
print(valuable_package)

