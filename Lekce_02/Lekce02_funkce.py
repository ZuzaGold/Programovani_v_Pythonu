
# def pozdrav():   #čistá funkce bez vedlejších vstupů
#     print("Ahoj!")

# pozdrav()

# def pozdrav(jmeno):
#     print(f"Ahoj {jmeno}")

# pozdrav("Jano")
# pozdrav("Katko")

# def soucet_cisel(a,b):
#     return a + b       # return = vrať mi, co je za "return" už se nezpracuje, return ukončí funkci

# vysledek = soucet_cisel(2, 9)
# print(vysledek)


smenny_kurz = 25

def smena_na_koruny(eura):
    return eura * smenny_kurz
print(smena_na_koruny(2))

def smena_na_koruny(eura, kurz):
    return eura * kurz
print(smena_na_koruny(2, 25))


def jeste_presne_nevim(vstup1, vstup2):
    pass   #dá pythonu příkaz, aby si nevšímal, že funkce není dopsaná. Například vím, že ji doplním později

def pozdrav(jmeno="clovece"):   #vezme tento argument, pokud mu neřeknu jinak
    print(F"Ahoj {jmeno}")      # v předchozím řádku jsme řekli clovece, pokud tam nebude zadne jmeno

pozdrav()
pozdrav("Terezo")



