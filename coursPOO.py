class Personne:
    compteur = 0  #Attributs de classe
    def __init__(self,fonction,age,nom): # Constructeur
        #Attributs d'instance
        self.fonction= fonction
        self.age = age
        self.nom = nom
        Personne.compteur +=  1
        # print("Création d'un objet")
    
    def __str__(self):
        return "mon objet: {}".format(self.fonction)


    def afficher(self): # Méthode
        print("------------------------")
        print("{} est {}, il a {} ans.".format(self.nom,self.fonction,self.age))
        print(self.nom,"est",self.fonction,", il a",self.age,"ans.")
    
    
# print("Le nombre d'objet créés:",Personne.compteur)

korri = Personne("Prof",45,"KORRI")
charles = Personne("étudiant",18,"Charles")
joalan = Personne("étudiant",17,"Joalan")


# pepe.age = 20
korri.afficher()
# print(korri)
# print(joalan)
charles.afficher()
joalan.afficher()
# print(Personne.fonction)
# print(Personne.age)

# print("------------------------")
# print(pepe.fonction)
# print(pepe.age)
# print("Le nombre d'objet créés:",Personne.compteur)
# # print("------------------------")
# # print(charles.fonction)
# # print(charles.age)
