import requests
import json

def get_info_by_ico():
    ico = input("Zadej IČ hledaného subjektu: ")

    url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"

    response = requests.get(url)

    data = response.json()

    print(json.dumps(data, indent=4, ensure_ascii=False))

    with open("domaci_ukol/obchodni_rejstriky.py/response.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    obchodni_jmeno = data.get('obchodniJmeno', 'N/A')
    textova_adresa = data.get('sidlo', {}).get('textovaAdresa', 'N/A')

    print(f"{obchodni_jmeno}\n{textova_adresa}")

get_info_by_ico()

