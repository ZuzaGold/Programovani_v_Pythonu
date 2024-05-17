import json

path = "Lekce_10/absolventi.json"

with open(path, encoding="utf-8") as file:
    absolvents = json.load(file)

#print(absolvents)
for i in absolvents:
    print(i["dochazka"])

#dump()
hours = {'po': 8, 'ut': 7, 'st': 6, 'ct': 10, 'pa': 4}
with open('hodiny.json', mode='w', encoding="utf-8") as file:
    json.dump(hours,file)

data = {"řeřicha": "Česká Třebová"}
with open("Lekce_10/rericha.json", mode="w", encoding="utf-8") as output_file:
    json.dump(data, output_file, ensure_ascii=False)

with open("Lekce_10/zavod.json", encoding="utf-8") as file:
    runners = json.load(file)
print(runners)
print(runners[0])
print(runners[0]["jmeno"])

