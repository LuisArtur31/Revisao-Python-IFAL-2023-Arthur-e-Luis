#Lista de Exercício 3 - Questão 14
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

class ParImpar:
    def __init__(self):
        self.numeros = []

    def ler_numeros(self):
        for i in range(10):
            while True:
                try:
                    numero = int(input(f"Digite o {i+1}º número inteiro: "))
                    self.numeros.append(numero)
                    break
                except ValueError:
                    print("Valor inválido. Digite um número inteiro válido.")

    def calcular_par_impar(self):
        pares = 0
        impares = 0

        for numero in self.numeros:
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1

        print(f"Quantidade de números pares: {pares}")
        print(f"Quantidade de números ímpares: {impares}")


def main():
    par_impar = ParImpar()
    par_impar.ler_numeros()
    par_impar.calcular_par_impar()


if __name__ == "__main__":
    main()
