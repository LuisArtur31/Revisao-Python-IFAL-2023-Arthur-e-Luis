#Lista de Exercício 1 - Questão 6
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math


class RaioInvalidoException(Exception):
    pass


class CalculadoraAreaCirculo:
    def __init__(self):
        self.raio = None

    def ler_raio(self):
        while True:
            try:
                self.raio = float(input("Digite o raio do círculo: "))
                if self.raio <= 0:
                    raise RaioInvalidoException("Raio inválido. Digite um valor positivo.")
                break
            except ValueError:
                print("Valor inválido. Digite um número.")
            except RaioInvalidoException as e:
                print(f"Erro: {str(e)}")

    def calcular_area(self):
        if self.raio is None:
            raise RaioInvalidoException("Nenhum raio foi informado.")

        area = math.pi * self.raio ** 2
        return area


def main():
    calculadora = CalculadoraAreaCirculo()

    try:
        calculadora.ler_raio()
        area = calculadora.calcular_area()
        print(f"A área do círculo é: {area:.2f}")
    except RaioInvalidoException as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
