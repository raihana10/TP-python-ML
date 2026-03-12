#classe Personne
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        
#classe Etudiant
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

    

#classe EtudiantGI
class EtudiantGI(Etudiant):
    def __init__(self , nom , age , option , **kwargs):
        super().__init__(nom, age, filiere='GI', niveau='GI2', **kwargs)
        self.option = option

    def afficher(self):
        super().afficher()
        print(f"Option:{self.option}")