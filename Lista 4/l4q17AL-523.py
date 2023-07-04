#Lista de Exercício 4 - Questão 17
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
#Atleta: Rodrigo Curvêllo
 
#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m

#Resultado final:
#Atleta: Rodrigo Curvêllo
#Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#Média dos saltos: 5.9 m

class Atleta:
    def __init__(self, nome):
        self.nome = nome
        self.saltos = []

    def adicionar_salto(self, distancia):
        self.saltos.append(distancia)

    def calcular_media_saltos(self):
        media = sum(self.saltos) / len(self.saltos)
        return media

    def mostrar_resultado(self):
        print("Resultado final:")
        print(f"Atleta: {self.nome}")
        print(f"Saltos: {' - '.join(map(str, self.saltos))}")
        media = self.calcular_media_saltos()
        print(f"Média dos saltos: {media} m")


def main():
    atletas = []

    while True:
        nome = input("Digite o nome do atleta (ou enter para encerrar): ")
        if not nome:
            break

        atleta = Atleta(nome)

        for i in range(1, 6):
            distancia = float(input(f"Digite a distância do {i}º salto: "))
            atleta.adicionar_salto(distancia)

        atletas.append(atleta)

    for atleta in atletas:
        print("\n")
        print("Atleta:", atleta.nome)
        for i, salto in enumerate(atleta.saltos, start=1):
            print(f"Salto {i}: {salto} m")
        atleta.mostrar_resultado()

    print("\nPrograma encerrado.")


if __name__ == "__main__":
    main()
