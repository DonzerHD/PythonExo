import turtle

# Ceci est un commentaire, les commentaires sont ignorés par l'ordinateur.
# Ils sont ici pour permettre aux développeur de garder leur code compréhensible 
# (pour eux même ou pour les autres)

turtle.speed(8) # permet de régler la vitesse d'animation de la tortue (1 étant le plus lent, 10 le plus rapide)

# Début des instructions permettant de dessiner : insérer votre code ici !
turtle.begin_fill()
def my_function(avancer , tourner):
    i = 0
    while i < 4 :
        turtle.forward(avancer)
        turtle.right(tourner)
        i = i + 1


my_function(200, 90)
# fin des instruction permettant de dessiner.

turtle.done() # permet d'indiquer à la tortue que nous avons fini le dessin

