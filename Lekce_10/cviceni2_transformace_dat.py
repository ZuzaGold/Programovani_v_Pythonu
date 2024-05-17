import json

words = {}

with open("Lekce_10/words.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        # words.sort()
        # words = line.split()
        letter= line.strip()[0]
        if letter in words:
            words[letter].append(line)
        else:
            words[letter] = [line]

with open("Lekce_10/output.json", mode="w", encoding="utf-8") as file:
          json.dump(words, json_file, indent=4, sort_keys=True)

          
# nefunguje, dopsat od Pavla