#Lista de Exercício 2 - Questão 16
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math


class ValorInvalidoException(Exception):
    pass


class EquacaoSegundoGrau:
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0

    def ler_coeficientes(self):
        try:
            self.a = float(input("Digite o valor de a: "))

            if self.a == 0:
                raise ValorInvalidoException("A equação não é do segundo grau. O valor de a não pode ser zero.")

            self.b = float(input("Digite o valor de b: "))
            self.c = float(input("Digite o valor de c: "))
        except ValueError:
            raise ValorInvalidoException("Valor inválido. Digite um número válido.")

    def calcular_delta(self):
        delta = self.b ** 2 - 4 * self.a * self.c
        return delta

    def calcular_raizes(self, delta):
        if delta < 0:
            raise ValorInvalidoException("A equação não possui raízes reais.")
        elif delta == 0:
            raiz = -self.b / (2 * self.a)
            return [raiz]
        else:
            raiz1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            raiz2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return [raiz1, raiz2]

    def imprimir_raizes(self, raizes):
        print("Raiz(es) da equação:")
        for raiz in raizes:
            print(raiz)


def main():
    try:
        equacao = EquacaoSegundoGrau()
        equacao.ler_coeficientes()
        delta = equacao.calcular_delta()
        raizes = equacao.calcular_raizes(delta)
        equacao.imprimir_raizes(raizes)
    except ValorInvalidoException as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
