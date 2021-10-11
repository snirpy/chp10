class Personne:
    
    def __init__(self, nom, prenom):
        print("appel constructeur!")
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self._lieu_residence = "Paris" # Notez le souligné _ devant le nom
    def _get_lieu_residence(self):
        print("On accède à l'attribut lieu_residence !")
        return self._lieu_residence

    def _set_lieu_residence(self, nouvelle_residence):
        print("Attention, il semble que {} déménage à {}.".format( \
                self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence

    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)


personne1 = Personne("KORRI","Ilyas")

# personne1.lieu_residence = "Madrid"
# personne1._set_lieu_residence("Clichy") #Equivalente à l'instruction précedente

personne1._lieu_residence = "Madrid" # modification sans passer par le setter

# print(personne1.lieu_residence)
# personne2 =Personne("Peng","Christope"
# print(personne1._get_lieu_residence)
# monAdresse = personne1._get_lieu_residence()
# print(monAdresse)


# print(f"J'habite à {personne1._lieu_residence}. # 'Avec _'")
# print(f"J'habite à {personne1.lieu_residence}. # 'sans _'")

maVille = personne1._get_lieu_residence()
print(f"J'habite à {maVille}.")

# print(f"J'habite à {personne1._lieu_residence}.")