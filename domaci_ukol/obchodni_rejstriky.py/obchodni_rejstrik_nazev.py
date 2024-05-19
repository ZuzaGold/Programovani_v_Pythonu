import requests
import json

def search_by_name():
    name = input("Zadej název subjektu: ")
    url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    data = json.dumps({"obchodniJmeno": name})

    print(f"Data odeslána v POST požadavku: {data}")

    response = requests.post(url, headers=headers, data=data)
    if response.status_code != 200:
        print(f"Chyba: {response.status_code} - {response.reason}")
        return

    data = response.json()

    print(json.dumps(data, indent=4, ensure_ascii=False))

    with open("domaci_ukol/obchodni_rejstriky.py/search_response.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    subjekty = data.get('ekonomickeSubjekty', [])

    if not subjekty:
        print("Nenalezen žádný subjekt.")
        return

    for subjekt in subjekty:
        obchodni_jmeno = subjekt.get('obchodniJmeno', 'N/A')
        ico = subjekt.get('ico', 'N/A')
        print(f"{obchodni_jmeno}, IČO: {ico}")

search_by_name()
