import csv

etudiants = [
    {"ID": 1, "Nom": "Schmitt", "Prénom": "Albert", "Note": 14},
    {"ID": 2, "Nom": "Al-Hakim", "Prénom": "Yasmine", "Note": 17},
    {"ID": 3, "Nom": "Tran", "Prénom": "Sebastien", "Note": 12},
    {"ID": 4, "Nom": "Meyer", "Prénom": "Claire", "Note": 16},
    {"ID": 5, "Nom": "Kobayashi", "Prénom": "Kaito", "Note": 11},
]

with open("donnees.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["ID", "Nom", "Prénom", "Note"])
    writer.writeheader()
    writer.writerows(etudiants)





with open("resultats.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Nom", "Prénom", "Résultat"])
    for etudiant in etudiants:
        resultat = "Admis" if etudiant["Note"] >= 10 else "Refusé"
        writer.writerow([etudiant["Nom"], etudiant["Prénom"], resultat])





data = []
with open("donnees.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        data.append([int(row[0]), row[1], row[2], int(row[3])])

print(data)
