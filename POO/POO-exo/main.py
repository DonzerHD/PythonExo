#Personne (entité -> class)
# Données : nom , age 
# Actions :  (méthodes)
# -SePresenter
# -DemanderNom (input)

class EtreVivant:
    ESPECE_ETRE_VIVANT = '(Etre vivant non identifié)'
    
    def AfficherInfosEtreVivant(self):
        print("Info être vivant : " + self.ESPECE_ETRE_VIVANT)

class Chat(EtreVivant):
    ESPECE_ETRE_VIVANT = "Chat (Mammifère félin)"
    
class Personne(EtreVivant):
    ESPECE_ETRE_VIVANT = "Humain (Mammifère Homo sapiens)"
    #Variable de classe
    
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
        
class Etudiant(Personne):
   def __init__(self, nom: str , age: int , etudes :str):
       super().__init__(nom, age)
       self.etudes = etudes
       
   def SePresenter(self):
        super().SePresenter()
        print("Je suis etudiant en " + self.etudes)
       
# --- UTILISATION ---

liste_personnes = [Personne("Thomas" , 22), 
                   Personne("Paul", 12), 
                   Personne("Paola", 48)]

for personne in liste_personnes:
    personne.SePresenter()
    personne.AfficherInfosEtreVivant()
    print()
    
chat = Chat()
chat.AfficherInfosEtreVivant()
etreVivant = EtreVivant()
etreVivant.AfficherInfosEtreVivant()

etudiant = Etudiant("Kevin" , 23 , 'Informaticien')
etudiant.AfficherInfosEtreVivant()
etudiant.SePresenter()

