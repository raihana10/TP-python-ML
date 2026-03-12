from classes.Etudiant import Etudiant
class EtudiantGI(Etudiant):
    def __init__(self , nom , age , option , **kwargs):
        super().__init__(nom, age, filiere='GI', niveau='GI2', **kwargs)
        self.option = option

    def afficher(self):
        super().afficher()
        print(f"Option:{self.option}")