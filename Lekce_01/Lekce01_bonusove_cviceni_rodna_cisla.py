rodna_cisla = [
    "845128/6219",
    "801002/5021",
    "900116/8291",
    "790501/7894",
    "850706/9259",
    "891222/1824",
    "870327/9582",
    "810602/6883",
    "850512/5070",
    "790531/7081"
]

# kolik přišlo mužů a žen do ordinace?
# jaký byl nejstarší a nejmladší pacient?

pocet_muzu = 0
pocet_zen = 0

nejstarsi_datum = "999999"
nejmladsi_datum = "000000"

for rodne_cislo in rodna_cisla:
    rok = rodne_cislo[:2]
    mesic = int(rodne_cislo[2:4])
    den = rodne_cislo[4:6]

    if mesic > 50:
        pohlavi = "žena"
        pocet_zen += 1
        mesic -=50
    else: 
        pohlavi = "muž"
        pocet_muzu += 1

    if mesic < 10:
        mesic_str = '0' + str(mesic)
    else:
        mesic_str = str(mesic)
    
    datum_narozeni = rok + mesic_str + den

    if datum_narozeni < nejstarsi_datum:
        nejstarsi_datum = datum_narozeni
    if datum_narozeni > nejmladsi_datum:
        nejmladsi_datum = datum_narozeni

#Úprava datum na formát dd.mm.yy
nejstarsi_datum = (
    nejstarsi_datum[4:] + "." + nejstarsi_datum[2:4] + "." + nejstarsi_datum[:2]
)
nejmladsi_datum = (
    nejmladsi_datum[4:] + "." + nejmladsi_datum[2:4] + "." + nejmladsi_datum[:2]
)

print("Počet mužů:", pocet_muzu)
print("Počet žen:", pocet_zen)
print("Nejstarší pacient se narodil:", nejstarsi_datum)
print("Nejmladsi pacient se narodil:", nejmladsi_datum)

