from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    position: str

    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}. "
    
denisa = Employee("Denisa", "progmatorka")
print(denisa)

@dataclass
class Manager(Employee):
    subordinates: int
    car: str

    def __str__(self):
        return super().__str__() + f"Ma {self.subordinates} podrizenych a auto {self.car}."
    
olga = Manager("Olga", "vedouci", 53, "modre")
print(olga)

print(isinstance(olga, Manager))  # TRUE  # dědí z vyšší třídy
# print(isinstance(olga, Employee)) stejný výsledek  TRUE

# print(isinstance(denisa, Manager))  FALSE

if hasattr(olga, "car"):
    print(olga.car)

# print(hasattr(olga, "car"))

print(getattr(olga, "car"))
