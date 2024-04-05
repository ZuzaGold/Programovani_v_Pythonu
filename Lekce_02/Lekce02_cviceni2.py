# jmeno = 'Zuzana'
# print(jmeno.lower())
# print(jmeno.upper())

# hodnoty = ['12', '1', '7', '-11']

# hodnota_na_treti_pozici = hodnoty[2]
# vysledek = int(hodnoty[2]) + 4
# hodnoty[2] = str(vysledek)
# print(hodnoty)



hodnoty = '12.1 1.68 7.45 -11.51'
seznam_cisel = hodnoty.split()
posledni_cislo = float(seznam_cisel[-1])+0.25
seznam_cisel[-1]= str(posledni_cislo)
upraveny_retezec = ' '.join(seznam_cisel)
print(upraveny_retezec)

# nove_hodnoty = hodnoty.split()
# upravene_cislo = float(nove_hodnoty[3] + 0.25)     # toto nefunguje
# upravene_cislo = str(upravene_cislo)
# dalsi_hodnoty = ' '.join(nove_hodnoty)
# print(dalsi_hodnoty)                              


