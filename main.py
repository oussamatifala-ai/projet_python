class Voiture:
    def __init__ (self,matricule,annee,marque,kilometrage):
        self.matricule=matricule
        self.annee=annee
        self.marque=marque
        self.kilometrage=kilometrage
        self.chauffeur=None
    def afficherInformations(self):
        print("matricule:", self.matricule)
        print("annee:", self.annee)
        print("marque:", self.marque)
        print("kilometrage:", self.kilometrage)
        if self.chauffeur is not None:
           print("chauffeur:", self.chauffeur.nom , self.chauffeur.prenom)
        else:
           print("Chauffeur:Aucun")
class Employe:
    def __init__(self,numeroPermis,nom,prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None
    def afficherInformations(self):
        print("Numero permis:", self.numeroPermis)
        print("Nom:", self.nom )
        print("Prenom:", self.prenom)
        
        if self.voitureService is not None
            print("Voiture:", self.voitureService.marque, self.voitureService.matricule)
        else:
            peint("Voiture: Aucune")
