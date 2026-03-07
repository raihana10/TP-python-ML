from classes.Personne import Personne
class Etudiant(Personne):
    def __init__(self, nom , age , filiere='GI' , niveau='GI2' , **kwargs):
        super().__init__(nom, age)
        self.filiere = filiere
        self.niveau = niveau
        self.notes = []
        self.infos_supplementaires = kwargs

    def ajouter_note(self, *args):
        for note in args:
            self.notes.append(note)

    def calculer_moyenne(self):
        if len(self.notes) == 0:
            return 0
        return sum(self.notes) / len(self.notes)

    def afficher(self):
        print(f"Nom:{self.nom}")
        print(f"Age:{self.age}")
        print(f"Filiere:{self.filiere}")
        print(f"Niveau:{self.niveau}")
        print(f"Notes:{self.notes}")
        print(f"Moyenne:{self.calculer_moyenne()}")
        if self.infos_supplementaires:
            print("====> Informations supplémentaires:")
            for key, val in self.infos_supplementaires.items():
                print(f"{key}:{val}")
