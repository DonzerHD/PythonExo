#Personne (entité -> class)
# Données : nom , age 
# Actions :  (méthodes)
# -SePresenter
# -DemanderNom (input)

# --- DEFINITION ---
#Si age == 0 => Bonjour , je m'appelle Toto
#            => On affiche pas mineur
#            => Demander nom a l'utilisateur
#            => DemanderNom(...)   - > input("")  -> nom
class Personne:
    def __init__(self, nom :str = "", age :int = 0):
        self.nom = nom #crée une variable d'instance : nom
        self.age = age
        if nom == "":
            self.DemanderNom()
        
    def SePresenter(self):
            if self.age == 0:
                print(f"Bonjour je m'appelle {self.nom}")                          
            else:
                print(f"Bonjour je m'appelle {self.nom} et j'ai {self.age} ans")
                if self.EstMajeur():
                    print("Je suis majeur")
                else:
                 print("Je suis mineur")
    
    # Est Majeur -> True / False
    def EstMajeur(self):
        return self.age >= 18
    
    def DemanderNom(self):
        self.nom = input("Quel est ton nom ?")
       
# --- UTILISATION ---

personne1 = Personne("Thomas" , 22) #Je cree une personne
personne2 = Personne("Paul", 12)

personne3 = Personne()
personne4 = Personne(age=22)

personne1.SePresenter()
personne2.SePresenter()
personne3.SePresenter()
personne4.SePresenter()



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