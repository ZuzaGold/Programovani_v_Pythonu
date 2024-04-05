velikonoce = {"klic" : "hodnoty",
              "Datum": "1. dubna 2024",
              "Symboly" : ["vajicko", "pomlazka", "beranek"],
              "Pocasi" : {"teplota" : "20", 
                          "oblacnost" : "jasno"},
              "Dalsi slovnik" : {"klic" : "hodnota"}}

print(velikonoce)
print(velikonoce["Datum"])
print(velikonoce["Symboly"])
print(velikonoce["Symboly"][1])
print(velikonoce["Pocasi"]["teplota"])

velikonoce["Pocasi"].update({"srazky": "zadne"})   # update je jen pro slovníky
print(velikonoce)

velikonoce["Symboly"].append("kuratko")            # append přidaly jsme položku do seznamu
print(velikonoce)



