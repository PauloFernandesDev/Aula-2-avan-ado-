class Pessoa():
    def __init__(self,peso, nome, idade):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.statusComendo = False
        self.statusFalando = False
        self.statusDormindo = False

    def comer(self, comida):
        if self.statusComendo == True:
            print(f"{self.nome} já está comendo!")
        elif self.statusFalando == True:
            print(f"{self.nome} não pode comer por que está falando!")
        elif self.statusDormindo == True:
            print(f"{self.nome} não pode comer por que está dormindo!")
        else:
            print(f"{self.nome} está comendo! {comida}")
            self.statusComendo = True

    def falar(self):
        if self.statusComendo:
            print(f"{self.nome} não pode falar por que está comendo!")
        elif self.statusFalando:
            print(f"{self.nome} já está falando!")
        elif self.statusDormindo:
            print(f"{self.nome} não pode falar por que está dormindo!")
        else:
            print(f"Olá, meu nome é {self.nome} e o seu? ")
            self.statusFalando = True


    def dormir(self):
        if self.statusComendo:
            print(f"{self.nome} não pode dormir por que está comendo!")
        elif self.statusFalando:
            print(f"{self.nome} não pode dormir por que está falando!")
        elif self.statusDormindo:
            print(f"{self.nome} já está dormindo!")
        else:
            print(f"{self.nome} foi dormir!")
            self.statusDormindo = True

    def pararComer(self):
            self.statusComendo = False
            print(f"{self.nome} Parou de comer!")

    def pararFalar(self):
            self.statusFalando = False
            print(f"{self.nome} Parou de Falar!")

    def pararDormir(self):
            self.statusDormindo = False
            print(f"{self.nome} Acordou!")