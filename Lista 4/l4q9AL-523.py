#Lista de Exercício 4 - Questão 9
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

class ListaNumeros:
    def __init__(self):
        self.numeros = []

    def ler_numeros(self):
        for i in range(10):
            while True:
                try:
                    numero = int(input(f"Digite o número {i+1}: "))
                    self.numeros.append(numero)
                    break
                except ValueError:
                    print("Valor inválido. Digite um número inteiro.")

    def calcular_soma_quadrados(self):
        soma_quadrados = sum([numero**2 for numero in self.numeros])
        return soma_quadrados

    def mostrar_numeros(self):
        print("Números:", self.numeros)

    def mostrar_soma_quadrados(self):
        soma_quadrados = self.calcular_soma_quadrados()
        print("Soma dos quadrados dos números:", soma_quadrados)


def main():
    vetor_numeros = ListaNumeros()
    vetor_numeros.ler_numeros()
    vetor_numeros.mostrar_numeros()
    vetor_numeros.mostrar_soma_quadrados()


if __name__ == "__main__":
    main()
