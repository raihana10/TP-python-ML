from .models import Etudiant, EtudiantGI
from .stats import afficher_stats, classement
from .utils import saisir_int, saisir_float, saisir_chaine

from tabulate import tabulate


#dict pour stocker les etudiants
etudiants={}


#fct pour ajouter un etudiant
def ajouter_etu():

    print(" * Pour ajouter un etudiant, veuillez entrer les informations suivantes:")

    nom=saisir_chaine("Nom: ", min_len=3)
    age=saisir_int("Age: " ,min_val=17)

    print(" * Information supplementaires (optionnelles):")

    kwargs={}

    email=saisir_chaine("Email: ",min_len=4,obligatoire=False)
    if email:
        kwargs['email']=email

    ville=saisir_chaine("Ville: ", min_len=2, obligatoire=False)
    if ville:
        kwargs['ville']=ville

    type_etu=saisir_int("Type d'etudiant (1=Etudiant, 2=EtudiantGI): ",min_val=1,max_val=2)
    if type_etu==2:
        option=saisir_chaine("Option: ", min_len=3)
        etudiants[nom]=EtudiantGI(nom, age, option, **kwargs)
    else:
        etudiants[nom]=Etudiant(nom, age, **kwargs)
    print(f"Etudiant {nom} ajouté avec succès!")


#fct pour ajouter des notes
def ajouter_notes():
    nom=saisir_chaine(" * Nom de l'etudiant: ", min_len=3)
    if nom not in etudiants:
        print("----> Etudiant non trouvé!")
        return
    
    nb_notes=saisir_int(" * Nombre de notes à ajouter: ", min_val=1,max_val=20)

    notes=[]

    for i in range(nb_notes):
        note=saisir_float(f"Note {i+1}: ", min_val=0, max_val=20)
        notes.append(note)

    etudiants[nom].ajouter_note(*notes)
    print(f"----> Notes ajoutées pour l'etudiant {nom}!")


#fct pour afficher ts les etudiants
def afficher_etus():
    if not etudiants:
        print("----> Aucun etudiant à afficher!")
        return
    print("**** La liste des etudiants: ****")
    data=[]
    for etu in etudiants.values():
        type_etu="EtudiantGI" if isinstance(etu, EtudiantGI) else "Etudiant"
        option = etu.option if isinstance(etu, EtudiantGI) else "-"
        notes = ", ".join(str(n) for n in etu.notes) if etu.notes else "Aucune note"
        data.append([
            etu.nom, 
            etu.age, 
            etu.filiere, 
            etu.niveau,
            type_etu, 
            option, 
            notes,
            f"{etu.calculer_moyenne():.2f}"
        ])

    headers=["Nom", "Age", "Filiere", "Niveau", "Type", "Option", "Notes", "Moyenne"]
    print(tabulate(data, headers=headers, tablefmt="rounded_outline"))
    

#fct pour rechercher un etudiant
def rechercher_etu():
    nom=saisir_chaine(" * Nom de l'etudiant à rechercher: ", min_len=3)
    if nom not in etudiants:
        print("----> Etudiant non trouvé!")
        return
    else:
        print("----> Etudiant trouvé:")
        data=[]
        etu=etudiants[nom]
        type_etu="EtudiantGI" if isinstance(etu, EtudiantGI) else "Etudiant"
        option = etu.option if isinstance(etu, EtudiantGI) else "-"
        notes = ", ".join(str(n) for n in etu.notes) if etu.notes else "Aucune note"
        data.append([
            etu.nom, 
            etu.age, 
            etu.filiere, 
            etu.niveau,
            type_etu, 
            option, 
            notes,
            f"{etu.calculer_moyenne():.2f}"
        ])
        headers=["Nom", "Age", "Filiere", "Niveau", "Type", "Option", "Notes", "Moyenne"]
        print(tabulate(data, headers=headers, tablefmt="rounded_outline"))
        
#fct pour supp un etudiant
def supprimer_etu():
    if not etudiants:
        print("----> Aucun etudiant à supprimer!")
        return
    nom=saisir_chaine(" * Nom de l'etudiant à supprimer: ")
    if nom not in etudiants:
        print("----> Etudiant non trouvé!")
        return

    del etudiants[nom]
    print(f"----> Etudiant {nom} supprimé avec succès!")


#menu
def afficher_menu():
    print("============================")
    print("       **** Menu ****")
    print("============================")
    print("1. Ajouter un étudiant")
    print("2. Ajouter des notes")
    print("3. Afficher tous les étudiants")
    print("4. Rechercher un étudiant")
    print("5. Afficher les statistiques ")
    print("6. Classer les étudiants par moyenne")
    print("7. Supprimer un étudiant")
    print("8. Quitter")


def main():
    while True:
        afficher_menu()
        choix=input("Choix: ")
        if choix=="1":
            ajouter_etu()
        elif choix=="2":
            ajouter_notes()
        elif choix=="3":
            afficher_etus()
        elif choix=="4":
            rechercher_etu()
        elif choix=="5":
            afficher_stats(etudiants)
        elif choix=="6":
            classement(etudiants)
        elif choix=="7":
            supprimer_etu()
        elif choix=="8":
            print("Au revoir!")
            break
        else:
            print("Choix invalide! Veuillez réessayer.")

if __name__=="__main__":
    main()