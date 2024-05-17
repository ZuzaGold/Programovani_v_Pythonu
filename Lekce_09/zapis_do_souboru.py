text = "Nechci tento text zapsat do souboru."

# with open("soubor.txt", mode="w", encoding="utf-8") as output_file:
#     print(text, file=output_file)

#with open("soubor.txt", mode="a", encoding="utf-8") as output_file:    # "a" je append, tedy přidá do souboru
#    print(text, file=output_file)

names = ["Zuzana", "Olga", "Martina"]
with open("ucastnictvo.txt", mode="w", encoding="utf-8") as output_file:
    for name in names:
        print(name, file=output_file)