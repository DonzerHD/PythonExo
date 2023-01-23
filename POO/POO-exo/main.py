#Personne (entité -> class)
# Données : nom , age 
# Actions :  (méthodes)
# -SePresenter
# -DemanderNom (input)

# --- DEFINITION ---
class Personne:
    def __init__(self, nom):
        print("Bonjour je m'appelle " + nom)
        
    def SePresenter(self):
        print("Bonjour je m'appelle toto")

# --- UTILISATION ---
personne1 = Personne("Toto") #Je cree une personne
personne1.SePresenter()


""" def afficher_information_personne(nom , age):
    print(f"La personne s'appelle {nom} et son age est {age} ans")
    
def demander_nom_personne():
    nom = input("Quel est votre nom ?")  
    return nom
    
nom1 = "Jean"
age1 = 31

nom2 = "Thomas"
age2 = 23

afficher_information_personne(nom1 , age1)
afficher_information_personne(nom2 , age2)

nom3 = demander_nom_personne()
afficher_information_personne(nom3, age2) """