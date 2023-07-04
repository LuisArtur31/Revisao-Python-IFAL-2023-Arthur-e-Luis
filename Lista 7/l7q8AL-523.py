#Lista de Exercício 7 - Questão 8
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def ver_bucho(self):
        if self.bucho:
            print(f"{self.nome} está com os seguintes alimentos no bucho:")
            for alimento in self.bucho:
                print(alimento)
        else:
            print(f"{self.nome} está com o bucho vazio.")

    def digerir(self):
        if self.bucho:
            print(f"{self.nome} está digerindo os alimentos...")
            self.bucho = []
        else:
            print(f"{self.nome} não tem nada para digerir.")


# Teste interativo
macaco1 = Macaco("Bob")
macaco2 = Macaco("Charlie")

print("Alimentando o macaco 1...")
macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco1.comer("Laranja")
macaco1.ver_bucho()

print("Alimentando o macaco 2...")
macaco2.comer("Cenoura")
macaco2.comer("Pêssego")
macaco2.ver_bucho()

print("Digerindo alimentos do macaco 1...")
macaco1.digerir()
macaco1.ver_bucho()

print("Digerindo alimentos do macaco 2...")
macaco2.digerir()
macaco2.ver_bucho()

# Testando o macaco canibal
print("Macaco 2 comendo o macaco 1...")
macaco2.comer(macaco1)

