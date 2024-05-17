# zamestnanec_1 = ["Jana", "programatorka", 25]
# zamestnanec_2 = ["Zuzana", "vyvojarka", 7]

# employee_1 = {"name": "Jan Novák",
#               "position": "konstruktér",
#               "holiday_entitlement": 25}
# employee_2 = {"name": "Klára Nová",
#               "position": "konstruktérka",
#               "holiday_entitlement": 25}

# days = 30

# def holiday_requirement(days):
#     if days > employee_1["holiday_entitlement"]:
#         employee_1["holiday_entitlement"] -= days
#         print("uzij si dovolenou")
#     else:
#         print("zustanes doma")

class Employee:
    def __init__(self, name, position, holiday_entitlement, gross_salary):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.gross_salary = gross_salary

    def get_info(self):
        return f"Zamestnanec {self.name} pracuje na pozici {self.position}."
    
    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Uzij si to"
        else: 
            return f"Bohužel, uz nemas narok, zbyva ti jen {self.holiday_entitlement} dni dovolene."

#   def __str__(self)   zabudovaná funkce
#       return f"Zaměstnanec{self.name} pracuje na pozici {self.position}."


    @property
    def net_salary(self):
        return self.gross_salary * (1 - 0.15)

frantisek = Employee("František", "prodavač", 9, 120000)
# print(frantisek.get_info())

# jitka = Employee("Jitka", "administrátorka", 25)
# print(jitka.get_info())

# print(frantisek.take_holiday(5))
# print(frantisek.take_holiday(35))

print(frantisek.net_salary)
