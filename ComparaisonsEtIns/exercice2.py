nombreUn = int(input("Entrez le 1er nombre :"))
nombreDeux = int(input("Entrez le 2eme nombre :"))
nombreTrois = int(input("Entrez le 3eme nombre :"))

if nombreUn > nombreDeux and nombreUn > nombreTrois:
    print(f"Le nombre Un : {nombreUn} est le plus grande des nombres ")
elif nombreDeux > nombreUn and nombreDeux > nombreTrois:
    print(f"Le nombre Deux : {nombreDeux} est le plus grande des nombres ")
else:
    print(f"Le nombre Trois : {nombreTrois} est le plus grande des nombres ")