# l’encapsulation est un principe qui consiste à protéger ou à cacher des données de certains objets. 
# Les niveaux de visibilité
# En d’autres termes, cela consiste à ne pas rendre possible l’accès à certains attributs depuis une instance d’une classe.
# private __ et protégés _
# - Les membres privés auxquels on ne peut accéder que depuis l’intérieur de la classe ;
# - Les membres protégés auxquels on ne peut accéder que depuis l’intérieur de la classe ou depuis une classe fille ;
# - Les membres publics auxquels on peut accéder depuis n’importe quelle instance (ou objet) de la classe ou d’une classe fille.


class Personne:
     def __init__(self,prenom , nom , age):
          self.__prenom = prenom
          self.__nom = nom
          self.__age = age
          
     def infos_personne(self):
         print(f"nom : {self.__nom} ,prenom : {self.__prenom} age {self.__age}")
       
     def get_age(self):
         return self.__age
       
     def set_age(self, age):
         self.__age = age
  
personne1 = Personne("Thomas" , "Lemay" , 21)
personne1.infos_personne()
personne1.set_age(12)
personne1.infos_personne()
print(f"L'age de la personne est {personne1.get_age()} ans")
  
class Personne:
      def __init__(self,prenom , nom , age):
          self.__prenom = prenom
          self.__nom = nom
          self.__age = age
          
      def infos_personne(self):
         print(f"nom : {self.__nom} ,prenom : {self.__prenom} age {self.__age}")
       
      # getter
      @property
      def age(self):
         return self.__age
      
      # setter
      @age.setter
      def age(self, age):
         self.__age = age
  
personne1 = Personne("Thomas" , "Lemay" , 21)
personne1.age = 10
print(personne1.age)
personne1.infos_personne()
  
  
