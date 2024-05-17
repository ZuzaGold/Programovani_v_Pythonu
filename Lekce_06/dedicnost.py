class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}"
    
# instance = Jmenotridy("prvni atribut", "druhy atribut")

class Manager(Employee):
    def __init__(self, name, position, subordinates, car):
        super().__init__(name, position)
        # self.name = name
        # self.position = position
        self.subordinates = subordinates
        self.car = car

    def __str__(self):
        return super().__str__() + "." + f"Ma {self.subordinates} podrizenych a ridi {self.car}"

janina = Manager("Janina", "reditelka kurzu", 55, "Tesla")
print(janina)

frantisek = Employee("Frantisek", "prodavač")
jitka = Employee("Jitka", "administrátorka")

print(frantisek)
print(jitka)

