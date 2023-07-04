#Lista de Exercício 4 - Questão 7
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

class VetorNumeros:
    def __init__(self):
        self.numeros = []

    def ler_numeros(self):
        for i in range(5):
            while True:
                try:
                    numero = int(input(f"Digite o número {i+1}: "))
                    self.numeros.append(numero)
                    break
                except ValueError:
                    print("Valor inválido. Digite um número inteiro.")

    def calcular_soma(self):
        soma = sum(self.numeros)
        return soma

    def calcular_multiplicacao(self):
        multiplicacao = 1
        for numero in self.numeros:
            multiplicacao *= numero
        return multiplicacao

    def mostrar_numeros(self):
        print("Números:", self.numeros)

    def mostrar_soma(self):
        soma = self.calcular_soma()
        print("Soma dos números:", soma)

    def mostrar_multiplicacao(self):
        multiplicacao = self.calcular_multiplicacao()
        print("Multiplicação dos números:", multiplicacao)


def main():
    vetor_numeros = VetorNumeros()
    vetor_numeros.ler_numeros()
    vetor_numeros.mostrar_numeros()
    vetor_numeros.mostrar_soma()
    vetor_numeros.mostrar_multiplicacao()


if __name__ == "__main__":
    main()
