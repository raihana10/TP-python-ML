def saisir_int(message, min_val=None, max_val=None):
    #None : si on ne veut pas det de limite 
    while True:
        try:
            valeur = int(input(message))
            if min_val is not None and valeur < min_val:
                print(f" Valeur trop petite. Minimum autorisé : {min_val}")
                continue
            if max_val is not None and valeur > max_val:
                print(f" Valeur trop grande. Maximum autorisé : {max_val}")
                continue
            return valeur
        except ValueError:
            print(" Erreur : veuillez entrer un nombre entier valide.")


def saisir_float(message, min_val=None, max_val=None):

    while True:
        try:
            valeur = float(input(message))
            if min_val is not None and valeur < min_val:
                print(f" Valeur trop petite. Minimum autorisé : {min_val}")
                continue
            if max_val is not None and valeur > max_val:
                print(f" Valeur trop grande. Maximum autorisé : {max_val}")
                continue
            return valeur
        except ValueError:
            print(" Erreur : veuillez entrer un nombre décimal valide.")

def saisir_chaine(message, min_len=1, max_len=None, obligatoire=True):
# obligatoire : pour obliger user a saisir si sa val est true 
    while True:
        valeur = input(message).strip()
        if obligatoire and len(valeur) == 0:
            print(" Ce champ est obligatoire, la saisie ne peut pas être vide.")
            continue
        if len(valeur) < min_len and obligatoire:
            print(f" Trop court. Longueur minimale : {min_len} caractère(s).")
            continue
        if max_len is not None and len(valeur) > max_len:
            print(f" Trop long. Longueur maximale : {max_len} caractère(s).")
            continue
        return valeur
