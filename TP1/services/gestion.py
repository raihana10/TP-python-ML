from classes.EtudiantGI import EtudiantGI
from classes.Etudiant import Etudiant

#dict pour stocker les etudiants
etudiants={}

#fct pour ajouter un etudiant
def ajouter_etu():

    print(" * Pour ajouter un etudiant, veuillez entrer les informations suivantes:")

    nom=input("Nom: ")
    age=int(input("Age: ")) 

    print(" * Information supplementaires (optionnelles):")

    kwargs={}

    email=input("Email: ")
    if email:
        kwargs['email']=email

    ville=input("Ville: ")
    if ville:
        kwargs['ville']=ville

    type_etu=input("Type d'etudiant (1=Etudiant, 2=EtudiantGI): ")
    if type_etu=="2":
        option=input("Option: ")
        etudiants[nom]=EtudiantGI(nom, age, option, **kwargs)
    else:
        etudiants[nom]=Etudiant(nom, age, **kwargs)
    print(f"Etudiant {nom} ajouté avec succès!")

#fct pour ajouter des notes
def ajouter_notes():
    nom=input(" * Nom de l'etudiant: ")
    if nom not in etudiants:
        print("----> Etudiant non trouvé!")
        return
    nb_notes=int(input(" * Nombre de notes à ajouter: "))
    notes=[]
    for i in range(nb_notes):
        note=float(input(f"Note {i+1}: "))
        notes.append(note)
    etudiants[nom].ajouter_note(*notes)
    print(f"----> Notes ajoutées pour l'etudiant {nom}!")

#fct pour afficher ts les etudiants
def afficher_etus():
    if not etudiants:
        print("----> Aucun etudiant à afficher!")
        return
    print("**** La liste des etudiants: ****")
    print("--------------------------------")
    for etu in etudiants.values():
        etu.afficher()
        print("--------------------------------")

#fct pour rechercher un etudiant
def rechercher_etu():
    nom=input(" * Nom de l'etudiant à rechercher: ")
    if nom not in etudiants:
        print("----> Etudiant non trouvé!")
        return
    else:
        print("----> Etudiant trouvé:")
        etudiants[nom].afficher()
    
#fct pour afficher les stats
def afficher_stats():
    print("\n**** Statistiques ****")
    if not etudiants:
        print("----> Aucun etudiant pour calculer les statistiques!")
        return
    
    moyennes=[]
    for etu in etudiants.values():
        moyennes.append(etu.calculer_moyenne())

    moy_generale=sum(moyennes)/len(moyennes)
    meilleure=max(moyennes)
    pire=min(moyennes)

    print(f"----> Moyenne générale: {moy_generale}")
    print(f"----> Meilleure moyenne: {meilleure}")
    print(f"----> Pire moyenne: {pire}")

#fct pour classer les etuds par moyenne
def classement():
    if not etudiants:
        print("----> Aucun etudiant pour le classement!")
        return
    
    etudiants_tries=sorted(etudiants.values(), key=lambda e: e.calculer_moyenne(), reverse=True)

    print("\n**** Classement des etudiants ****")

    for i, etu in enumerate(etudiants_tries,1):
        print(f"{i}. {etu.nom} --> Moyenne: {etu.calculer_moyenne()}")

#fct pour supp un etudiant
def supprimer_etu():
    if not etudiants:
        print("----> Aucun etudiant à supprimer!")
        return
    nom=input(" * Nom de l'etudiant à supprimer: ")
    if nom not in etudiants:
        print("----> Etudiant non trouvé!")
        return
    del etudiants[nom]
    print(f"----> Etudiant {nom} supprimé avec succès!")