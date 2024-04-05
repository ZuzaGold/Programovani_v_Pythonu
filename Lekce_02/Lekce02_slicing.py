venecky = [1, 2, 4, 1, 6, 0, 1]

# print(venecky[0])

# venecky[0] = 3   # změní první položku
# print(venecky)

# print(venecky[0:5])
# print(venecky[:5])
# print(venecky[5:])
# print(venecky[::2])  # vezme každý druhý záznam
# print(venecky[1:5:2])  # vezme každý druhý zázanm

# print(len(venecky))
# print(sum(venecky))
# print(min(venecky))
# print(max(venecky))
# print(sorted(venecky))

retezec = "Mate radsi more, nebo hory?"
print(len(retezec))
#print(sum(retezec))
print(min(retezec))
print(max(retezec))
print(sorted(retezec))
print(sorted(retezec, reverse=True))

inzerat ="Na pracovní pozici se používá Python."
if "Python" in inzerat:
    print("Beru to!")

inzerat ="Na pracovní pozici se používá R."
if "Python" not in inzerat:
    print("Neberu to")



