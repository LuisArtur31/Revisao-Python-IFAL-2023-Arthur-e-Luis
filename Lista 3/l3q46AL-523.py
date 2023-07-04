#Lista de Exercício 3 - Questão 46
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
#Atleta: Rodrigo Curvêllo

#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m

#Melhor salto:  6.5 m
#Pior salto: 5.3 m
#Média dos demais saltos: 5.9 m

#Resultado final:
#Rodrigo Curvêllo: 5.9 m

class Atleta:
    def __init__(self, nome):
        self.nome = nome
        self.saltos = []

    def solicitar_saltos(self):
        print(f"Atleta: {self.nome}\n")
        for i in range(1, 6):
            while True:
                try:
                    salto = float(input(f"Digite o valor do {i}º salto: "))
                    break
                except ValueError:
                    print("Valor inválido. Digite um número válido.")
            self.saltos.append(salto)
        print()

    def calcular_media_saltos(self):
        self.saltos.sort()
        melhor_salto = self.saltos[-1]
        pior_salto = self.saltos[0]
        saltos_restantes = self.saltos[1:4]
        media = sum(saltos_restantes) / 3
        print(f"Melhor salto: {melhor_salto} m")
        print(f"Pior salto: {pior_salto} m")
        print(f"Média dos demais saltos: {media:.2f} m\n")

    def exibir_resultado_final(self):
        print("Resultado final:")
        print(f"{self.nome}: {sum(self.saltos) / 5:.2f} m\n")


def main():
    atletas = []
    while True:
        nome = input("Digite o nome do atleta (ou deixe em branco para sair): ")
        if not nome:
            break
        atleta = Atleta(nome)
        atleta.solicitar_saltos()
        atleta.calcular_media_saltos()
        atletas.append(atleta)

    for atleta in atletas:
        atleta.exibir_resultado_final()


# Execução do programa
if __name__ == '__main__':
    main()
