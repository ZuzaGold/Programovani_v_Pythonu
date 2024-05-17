#cislo = 100
#cislo = cislo + 1
#print(cislo)
#


#cislo = int(input("Zadej sto"))
#print(cislo)
#dalsi_cislo = int(1)
#total_cislo = cislo + dalsi_cislo
#print(f"celkové číslo je {total_cislo}")

#F = int(input("zadej hodnotu z kuchařky"))
#C=5*(F-32)/9
#print(f"převedeno na stupně celsia je {C}")

#ASI JSEM DĚLALA NAVÍC - Cvičení: Seznamy - pohyby na účtu / průměr / rozpětí

#pohyby = [1200, -250, -800, 540, 721, -613, -222]
#tady bude výsledek hodnota třetí v pořadí
#print(pohyby [2])

#tady budou všec hny kromě prvních dvou
#print(pohyby [2:6])

#tady bude počet všech výběrů
#print(len(pohyby))

#tady bude nejvyšší pohyb
#print(max(pohyby))

#tady bude nejnižší pohyb
#print(min(pohyby))

#tady bude celkový přírůstek na účtu za dané období
#print(sum(pohyby))


#s = [2, 3, 4, 5, 6]
#s = [1,2,3,4,5,6,7]
#s = [8,2,3,4,5,6,2,1]
#average = sum(s)/len(s)
#print(average)
#minimalni_hodnota = min(s)
#print(minimalni_hodnota)
#maximalni_hodnota = max(s)
#print((maximalni_hodnota)-(minimalni_hodnota))



#VRACÍM SE ZPĚT K PRVNÍMU BLOKU PŘÍKLADY NA PROCVIČOVÁNÍ
     #SOUČET ČÍSEL V SEZNAMU / NEJVĚTŠÍ PRVEK V SEZNAMU /
     #SUDÁ ČÍSLA / ROZDĚLENÍ ČÍSEL / ODSTRANĚNÍ DUPLIKÁTŮ / 
     #PŘIJÍMAČKY / RODNÁ ČÍSLA

cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#seznam = [2, 3, 4, 6, 7, 8, 11, 13, 12]
#seznam_soucet = [2+3+4+6+7+8+11+13+12]
#print(seznam_soucet)
#print(len(seznam))
#seznam_novy = seznam([0]+[1]+[2]+[3]+[4]+[5]+[6]+[7]+[8]+[9])
#print(seznam_novy)

    # pořád špatně

#Největší prvek v seznamu bez funkce max()
#sestupne_serazeno = sorted(seznam, reverse=True)
#print(sestupne_serazeno)
#print(sestupne_serazeno[0])

jina_cisla = [1,2,3,4,5]

soucet = 0
for jine_cislo in jina_cisla:
    soucet += jine_cislo
print("Součet čísel je:", soucet)

nova_cisla = [5, 3, 8, 1, 9, 2, 7]
nejvetsi_prvek = nova_cisla[0]
for nove_cislo in nova_cisla:
    if nove_cislo > nejvetsi_prvek:
        nejvetsi_prvek = nove_cislo
print("Největší prvek je:", nejvetsi_prvek)


#sudá čísla ze seznamu
#suda_cisla = 
#for cislo in seznam:
#    if cislo % 2 == 0:
#        print(cislo)

#suda_cisla = [cislo for cislo in seznam if cislo % 2 == 0]
#print(suda_cisla)


#rozdělení na sudá a lichá čísla

#licha_cisla = [cislo for cislo in seznam if cislo % 2 != 0]
#print("Lichá čísla ze seznamu: ", licha_cisla)

#suda_cisla = [cislo for cislo in seznam if cislo % 2 == 0]
#licha_cisla = [cislo for cislo in seznam if cislo % 2 != 0]
#print("Toto jsou sudá čísla: ", suda_cisla)
#print("Toto jsou lichá čísla: ", licha_cisla)

suda_cisla = []
licha_cisla = []

for cislo in cisla:
    if cislo % 2 == 0:
        suda_cisla.append(cislo)
    else:
        licha_cisla.append(cislo)
print("Seznam sudých čísel:", suda_cisla)
print("Seznam lichých čísel:", licha_cisla)



#odstranění duplikátů
# novy_seznam = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9, 9]
# bez_duplikatu = []
# for prvek in novy_seznam:
#     if prvek not in bez_duplikatu:
#         bez_duplikatu.append(prvek)
# print("Nový seznam bez duplicit:", bez_duplikatu)








