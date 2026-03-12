from .models import Etudiant, EtudiantGI
from tabulate import tabulate

#fct pour afficher les stats
def afficher_stats(etudiants):
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

    data = [
        ["Nombre d'étudiants", len(etudiants)],
        ["Moyenne générale",   f"{moy_generale}"],
        ["Meilleure moyenne",  f"{meilleure}"],
        ["Pire moyenne",       f"{pire}"],
    ]

    print(tabulate(data, tablefmt="rounded_outline"))

    

#fct pour classer les etuds par moyenne
def classement(etudiants):
    print("\n**** Classement des etudiants ****")
    if not etudiants:
        print("----> Aucun etudiant pour le classement!")
        return
    
    tri_etus=sorted(
        etudiants.values(), 
        key=lambda e: e.calculer_moyenne(), 
        reverse=True
    )

    for i, etu in enumerate(tri_etus,1):
        print(f"{i}. {etu.nom} --> Moyenne: {etu.calculer_moyenne()}")