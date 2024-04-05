# znamky = {
#     "Český jazyk": 1,
#     "Matematika": 2,
#     "Dějepis": 3,  
# }

# print(znamky)


# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
# }

# sales["Noc, která mě zabila"] = 0
# print(sales)

# sales["Vrah zavolá v deset"] += 100
# print(sales)


# tombola = {
#     7: "Láhev kvalitního vína Château Headache",
#     15: "Pytel brambor z místního družstva",
#     23: "Čokoládový dort",
#     47: "Kniha o historii města",
#     55: "Šiška salámu",
#     67: "Vyhlídkový let balónem",
#     79: "Moderní televizor",
#     91: "Roční předplatné městského zpravodaje",
#     93: "Společenská hra Sázky a dostihy",
# }

# cislo_listku = int(input("Jaké je číslo tvého lístku: "))

# if cislo_listku in tombola:
#     print("Gratulujeme! Vyhráváš:", tombola[cislo_listku])
# else:
#     print("Bohužel nevyhráváš nic!")


passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

jmeno_hosta = input("Zadej jméno hosta: ")

if jmeno_hosta in passwords:
    zadane_heslo = input("Zadej heslo: ")
    if zadane_heslo == passwords[jmeno_hosta]:
        print("Smíš vstoupit.")
    else:
        print("Nesprávné heslo.")
else:
    print("Host není na seznamu.")

    

    
