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
        
        if self.voitureService is not None:
            print("Voiture:", self.voitureService.marque, self.voitureService.matricule)
        else:
            print("Voiture: Aucune")

    def affecterVoiture(self, voiture):
        if self.voitureService is not None:
            print("Erreur: cet employe possede deja une voiture")
        elif voiture.chauffeur is not None:
            print("Erreur: cette voiture est deja attribuee")
        else:
            self.voitureService = voiture
            voiture.chauffeur = self
            print("Voiture attribuee avec succes")

    def retirerVoiture(self):
        if self.voitureService is None:
            print("Aucune voiture a retirer")
        else:
            self.voitureService.chauffeur = None
            self.voitureService = None
            print("Voiture retiree avec succes")