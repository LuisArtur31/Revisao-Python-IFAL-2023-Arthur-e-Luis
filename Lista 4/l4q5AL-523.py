#Lista de Exercício 4 - Questão 5
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

class Numeros:
    def __init__(self):
        self.numeros = []
        self.pares = []
        self.impares = []

    def ler_numeros(self):
        for i in range(20):
            while True:
                try:
                    numero = int(input(f"Digite o número {i+1}: "))
                    self.numeros.append(numero)
                    break
                except ValueError:
                    print("Valor inválido. Digite um número inteiro.")

    def separar_pares_impares(self):
        for numero in self.numeros:
            if numero % 2 == 0:
                self.pares.append(numero)
            else:
                self.impares.append(numero)

    def mostrar_vetores(self):
        print("Vetor de números:", self.numeros)
        print("Vetor de números pares:", self.pares)
        print("Vetor de números ímpares:", self.impares)


def main():
    numeros = Numeros()
    numeros.ler_numeros()
    numeros.separar_pares_impares()
    numeros.mostrar_vetores()


if __name__ == "__main__":
    main()
