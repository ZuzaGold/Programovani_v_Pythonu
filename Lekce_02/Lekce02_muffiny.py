def vyrob_muffiny(pocet_muffinu, specialni_ingredience=[]):
    print(f"Vyrábím {pocet_muffinu} muffinů.")
    if specialni_ingredience:         # může být zapsáno jako if specialni_ingredience:
        print(f"Přidávám speciální ingredience: {specialni_ingredience}")
    else:
        print("Bez speciálních ingrediencí")
    return pocet_muffinu
    

pocet = vyrob_muffiny(40, ["čokoláda", "vanilka"])
print(f"Celkově vyrobeno: {pocet} muffinů.")

# vyrábím 5 muffinů
# Přidávám speciální ingredience: čokoláda, vanilka
# Celkově vyrobeno: 5 muffinů