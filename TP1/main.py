from services import gestion

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
            gestion.ajouter_etu()
        elif choix=="2":
            gestion.ajouter_notes()
        elif choix=="3":
            gestion.afficher_etus()
        elif choix=="4":
            gestion.rechercher_etu()
        elif choix=="5":
            gestion.afficher_stats()
        elif choix=="6":
            gestion.classement()
        elif choix=="7":
            gestion.supprimer_etu()
        elif choix=="8":
            print("Au revoir!")
            break
        else:
            print("Choix invalide! Veuillez réessayer.")

main()