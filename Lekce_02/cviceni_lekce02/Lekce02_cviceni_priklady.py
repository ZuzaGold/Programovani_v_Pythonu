radky = [
    [2001, 7.8],
    [2002, 8.7],
    [2003, 8.2],
    [2004, 7.8],
    [2005, 7.7],
    [2006, 8.2],
    [2007, 9.1],
    [2008, 8.9],
    [2009, 8.4],
    [2010, 7.2]
]

sloupce = [
    [radka[0] for radka in radky],
    [radka[1] for radka in radky]
]

teplota_treti_radka = radky[2][1]
print("Teplota na třetím řádku:", teplota_treti_radka)

rok_paty_radka = radky[4][0]
print("Rok na pátém řádku?", rok_paty_radka)

posledni_radka = radky[-1]
print("Poslední řádek tabulky:", posledni_radka)

bez_prvnich_dvou_radku = radky[2:]
print("Tabulka bez prvních dvou řádků:")
for radka in bez_prvnich_dvou_radku:
    print(radka)

prvni_dva_radky = radky[:2]
print("Tabulka pouze z prvních dvou řádků:")
for radka in prvni_dva_radky:
    print(radka)

radky_5678 = radky[4:8]
print("Tabulka obsahující řádky 5, 6, 7, 8:")
for radka in radky_5678:
    print(radka)

sestupne_serazene_teploty = sorted(sloupce[1])
print("Seřazené teploty vzestupně:", sestupne_serazene_teploty)


