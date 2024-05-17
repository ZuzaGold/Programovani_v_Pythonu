with open("Lekce_09/mereni.txt", encoding="utf-8") as file:
    text = file.read()

print(text)

# toto je způsob jak to jenom otevřít, ale zůstane to otevřené, proto to teď nechceme
# file = open("Lekce_09/mereni.txt", encoding="utf-8")   # encoding... znamená dostat se k českým znakům
# print(file.read())

lines = []

with open("Lekce_09/mereni.txt", encoding="utf-8") as file:
    for line in file:                                           # tzv. for cyklus
        lines.append(line)
print(lines)


with open("Lekce_09/mereni.txt", encoding="utf-8") as file:     # to samé jako for cyklus, ale čistší verze
    text = file.readlines()

print(text)


output = []
with open("Lekce_09/mereni.txt", encoding="utf-8") as file:
    for line in file:
        day, temp = line.split('\t')
        output.append([day, float(temp)])
    print(output)
                   
                   
                   