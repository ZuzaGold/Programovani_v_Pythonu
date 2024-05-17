filename = input("Zadej název souboru: ")
with open(filename, mode="w", encoding="utf-8") as output_file:
    text = input("Zadej text: ")     
    print(text, file=output_file)


