znamky = [
    ['A', 9, 7, 8, 5],
    ['B', 5, 3, 6, 6],
    ['C', 8, 4, 9, 7],
    ['D', 8, 5, 4, 8],
    ['E', 10, 6, 10, 7]
]

bodovaci_tabulka = {
    1: range(36, 101),
    2: range(32, 36),
    3: range(26, 32),
    4: range(20, 26),
    5: range(0, 20)
}

for student in znamky:
    celkove_body = sum(student[1:])
    for zn, body_range in bodovaci_tabulka.items():
        if celkove_body in body_range:
            student.append(zn)
            break

prumerne_body_otazek = []
for i in range(1, 5):
    prumer_otazky = sum(student[i] for student in znamky) / len(znamky)
    prumerne_body_otazek.append((i, prumer_otazky))

nejvyssi_prumer = max(prumerne_body_otazek, key=lambda x: x[1])
nejnizsi_prumer = min(prumerne_body_otazek, key=lambda x: x[1])

print("Průměrné body z jednotlivých otázek:")
for otazka, prumer in prumerne_body_otazek:
    print(f"Otázka {otazka}: {prumer}")

print(f"Nejvíce bodů v průměru studenti dostali z otázky {nejvyssi_prumer[0]}.")
print(f"Nejméně bodů v průměru studenti dostali z otázky {nejnizsi_prumer[0]}.")
