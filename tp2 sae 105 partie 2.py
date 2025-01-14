import json

fiche = {
    "Nom": "Weber",
    "Prenom": "Charlotte",
    "age": 32,
    "profession": "ingénieure",
    "langues": ["Français", "Anglais", "Japonais"]
}

with open("donnees.json", mode="w", encoding="utf-8") as file:
    json.dump(fiche, file, ensure_ascii=False, indent=4)


    
with open("donnees.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)

print(data)
print(f"Type of data: {type(data)}")


data["adresse"] = "17, Grand’Rue – 68000 COLMAR"

with open("donnees.json", mode="w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
