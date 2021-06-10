
def afficher_resultat(rnombre):
    if (rnombre % 2) == 0:
        print("Le nombre que vous avez choisi " + str(rnombre) + " est pair")
    else:
        print("Le nombre que vous avez choisi " + str(rnombre) + " est impair")


def demander_nombre():
    nombre_int = ""
    while nombre_int == "":
        nombre_str = input(" Veuillez entrer un nombre ")
        try:
            nombre_int = int(nombre_str)
        except:
            print("ERREUR: Vous devez entrer un nombre pour continuer")
    return nombre_int


nombre = demander_nombre()
afficher_resultat(nombre)

