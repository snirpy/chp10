class Animal:
    def __init__(self,nom) :
        self.nom = nom
        self.nage = "OUI"
    
    def seDeplacer(self):
        print(f"Le {self.nom} se déplace")

    def seNourir(self):
        print(f"Le {self.nom} se nourit")

    def crier(self):
        print(f"Le {self.nom} crie")

class Carnivore(Animal):
    def __init__(self, nom,crie,deplacement,nourriture):
        super().__init__(nom)
        self.crie = crie
        self.deplacement = deplacement
        self.nourriture = nourriture

    def seDeplacer(self):
        print(f"Le {self.nom} {self.deplacement}")

    def seNourir(self):
        print(f"Le {self.nom} est un {self.nourriture} ")

    def crier(self):
        print(f"Le {self.nom} {self.crie}")

class Lion(Carnivore):
    def __init__(self, nom, crie, deplacement, nourriture,peaux):
        super().__init__(nom, crie, deplacement, nourriture)
        self.peaux = peaux
    
    def seCouvrir(self):
        print(f"Le {self.nom} a un {self.peaux}")

    def nager(self):
        print(f"Sait-t-il nager?: {self.nage}")

        
print("*"*20+"Classe Animal")

unAnimal = Animal("lion")
unAnimal.seDeplacer()
unAnimal.seNourir()
unAnimal.crier()

print("*"*20+"Classe Carnivore")

unAnimal = Carnivore("lion","rugit","court","carnivore")
unAnimal.seDeplacer()
unAnimal.seNourir()
unAnimal.crier()

print("*"*20+"Classe Animal")

unAnimal = Animal("lion")
unAnimal.seDeplacer()
unAnimal.seNourir()
unAnimal.crier()

print("*"*20+"Classe Lion")

unAnimal = Lion("lion","rugit","court","carnivore","pelage")
unAnimal.seDeplacer()
unAnimal.seNourir()
unAnimal.crier()
unAnimal.seCouvrir()
unAnimal.nager()
