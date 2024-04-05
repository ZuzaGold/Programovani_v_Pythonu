pocet_vstupenek = int(input("Kolik chces vstupenek? "))
#print(pocet_vstupenek)
cena_vstupenky = 9

celkova_cena = pocet_vstupenek * cena_vstupenky

if celkova_cena > 500:
    sleva = 0.1
    cena_po_sleve = celkova_cena * (1 - sleva)
elif celkova_cena < 10:
    print("to nemyslis vazne, za tolik si nic nekoupis. ")
else:
    print("Utrat vic, dostanes slevu")
print(celkova_cena)

#print(cena_po_sleve)


    



