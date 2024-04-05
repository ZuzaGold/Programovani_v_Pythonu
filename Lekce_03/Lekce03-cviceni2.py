import math


# school_report = {
#     "Český jazyk": 1,
#     "Anglický jazyk": 1,
#     "Matematika": 1,
#     "Přírodopis": 2,
#     "Dějepis": 1,
#     "Fyzika": 2,
#     "Hudební výchova": 4,
#     "Výtvarná výchova": 2,
#     "Tělesná výchova": 3,
#     "Chemie": 4,
# }

# prumer = sum(school_report.values()) / len(school_report)
# print("průměrná známka: ", prumer)
# print("Předměty se známkou 1: ")
# for predmet, znamka in school_report.items():
#     if znamka == 1:
#         print(predmet)


# books = [
#     {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
#     {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
#     {"title": "Past", "pages": 390, "rating": 4},
#     {"title": "Popel popelu", "pages": 411, "rating": 10},
#     {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
#     {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
#     {"title": "Zločinný steh", "pages": 542, "rating": 8},
#     {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
#     {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
# ]

# celkem_stran = 0
# for book in books:
#     celkem_stran += book["pages"]
# print("Celkový počet přečtených stran: ", celkem_stran)

# print(sorted(books[0]))

for count, i  in enumerate(books):
    print(count, i)


# pocet_knih_s_vysokym_hodnocenim = 0
# for book in books:
#     if book["rating"] >= 8:
#         pocet_knih_s_vysokym_hodnocenim += 1
# print("Počet knih s hodnocením alespoň 8: ", pocet_knih_s_vysokym_hodnocenim)


# plates = {"4A2 3000": "František Novák",
#     "6P5 4747": "Jana Pilná",
#     "3B7 3652": "Jaroslav Sečkár",
#     "1P5 5269": "Marta Nováková",
#     "37E 1252": "Martina Matušková",
#     "2A5 2241": "Jan Král"}

# # klíč: poznávací značka
# # hodnota: jméno

# for plate, owner in plates.items():
#     if plate[1] == "P":
#         print(owner)

recept = {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}

# pro tento příklad byla importována "math"

celkova_cena = 0

for ingredience in recept['ingredience']:
    cena = ingredience[2].split()[0]
    celkova_cena += float(cena)

print(f"Celková cena jídla: {math.ceil(celkova_cena)} Kč")



