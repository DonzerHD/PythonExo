# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
noms = []
for i in range(3):
    noms.append(Personne(input(f"nom de la personne {i+1} : ")))

for nom in noms:
    nom.SePresenter()
