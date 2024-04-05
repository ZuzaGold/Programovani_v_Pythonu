import math
import statistics

# cislo = 25.3
# print(math.floor(cislo))    #zaokrouhlení dolů
# print(math.ceil(cislo))     #zaokrouhlení nahoru
# print(round(cislo))         # Pythonovské zaokrouhlování


# school_report = [
#     ["Český jazyk", 1],
#     ["Anglický jazyk", 1],
#     ["Matematika", 1],
#     ["Přírodopis", 2],
#     ["Dějepis", 1],
#     ["Fyzika", 2],
#     ["Hudební výchova", 4],
#     ["Výtvarná výchova", 2],
#     ["Tělesná výchova", 3],
#     ["Chemie", 4],
# ]

# vybrane_znamky = []
# for predmet, znamka in school_report:
#     if predmet in ["Český jazyk", "Anglický jazyk", "Matematika", "Fyzika"]:
#         vybrane_znamky.append(znamka)

# prumer = statistics.mean(vybrane_znamky)
# nejlepsi_znamka = max(vybrane_znamky)
# nejhorsi_znamka = min(vybrane_znamky)

# print("Průměr studenta:", prumer)
# print("Nejlepší známka:", nejlepsi_znamka)
# print("Nejhorší známka:", nejhorsi_znamka)


votes = [                                      
    "curling", 
    "vánoční svařák na trzích", 
    "vánoční svařák na trzích", 
    "curling", 
    "zážitková první pomoc",
    "curling", 
    "zážitková první pomoc",
    "curling",
    "zážitková první pomoc",
    ]

#  modus = nejcastejsi akce, název modusu je mode()  /  data v seznamech = votes

nejcastejsi_akce = statistics.mode(votes)
print("Nejčastější aktivita:", nejcastejsi_akce)
