with open("kalendar.txt", mode="w", encoding="utf-8") as output_file:
     print(file=output_file)

pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
with open("kalendar.txt", mode="a", encoding="utf-8") as output_file:
     for pocet_dni in pocty_dni:
        print(pocet_dni, file=output_file)
        # jde zapsat také takto:  file.write(f"{item}\n")
