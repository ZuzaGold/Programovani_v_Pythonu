import requests

path = "https://api.kodim.cz/python-data/people"

response = requests.get(path)
#print(response)
data = response.json()
#print(data)
#print(len(data))
people_count = len(data)
print(f"celkem lidí: {people_count}")

#for items in data:
#    print(items)

print(data[0].keys())


female_count = 0
for person in data:
    if person["gender"] == "Female":
        female_count += 1

f_count = sum ([1 for person in data if person["gender"]== "Female"])

print(f"V souboru je {female_count} žen.")
print(f"Počet mužů je {people_count - female_count}.")


# Zjistěte kolik lidí celkem seznam obsahuje.    
# Zjistěte jaké všechny informace máme o jednotlivých osobách.
# Zjistěte, kolik je v souboru mužů a žen.
