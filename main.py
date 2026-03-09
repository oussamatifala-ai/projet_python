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

e1 = Employe("P123", "Oussama", "Tifala")
e2 = Employe("P456", "Ali", "Karim")
e3 = Employe("P789", "Sara", "Amine")

v1 = Voiture("AA111", 2022, "Toyota", 30000)
v2 = Voiture("BB222", 2021, "Honda", 45000)
v3 = Voiture("CC333", 2020, "Ford", 60000)

print("=== Employes ===")
e1.afficherInformations()
e2.afficherInformations()
e3.afficherInformations()

print("=== Voitures ===")
v1.afficherInformations()
v2.afficherInformations()
v3.afficherInformations()
# Affectation des voitures aux employes
print("=== Affectation des voitures ===")
e1.affecterVoiture(v1)
e2.affecterVoiture(v2)
print("=== Apres affectation ===")
e1.afficherInformations()
e2.afficherInformations()
e3.afficherInformations()

v1.afficherInformations()
v2.afficherInformations()
v3.afficherInformations()

print("=== Retrait de voiture ===")
e1.retirerVoiture()

print("=== Apres retrait ===")
e1.afficherInformations()
v1.afficherInformations()
# Test d affectation interdite
print("=== Test d affectation interdite ===")
e3.affecterVoiture(v2)