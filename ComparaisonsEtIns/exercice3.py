annee = int(input("Entrez l'année de votre choix :"))
bl = True
if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0 : 
    print("Cette année est bissextile")
else:
    print("Cette année n'est pas bissextile")
    