#Lista de Exercício 1 - Questão 11
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo.
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

class Calculadora:
    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.num3 = None

    def ler_numeros(self):
        try:
            self.num1 = int(input("Digite o primeiro número inteiro: "))
            self.num2 = int(input("Digite o segundo número inteiro: "))
            self.num3 = float(input("Digite um número real: "))
        except ValueError:
            print("Erro: Digite apenas números válidos.")
            self.ler_numeros()

    def calcular_produto(self):
        return (self.num1 * 2) * (self.num2 / 2)

    def calcular_soma(self):
        return (self.num1 * 3) + self.num3

    def calcular_potencia(self):
        return self.num3 ** 3

    def executar_calculos(self):
        self.ler_numeros()
        produto = self.calcular_produto()
        soma = self.calcular_soma()
        potencia = self.calcular_potencia()

        print(f"O produto do dobro do primeiro com metade do segundo é: {produto}")
        print(f"A soma do triplo do primeiro com o terceiro é: {soma}")
        print(f"O terceiro elevado ao cubo é: {potencia}")


calculadora = Calculadora()
calculadora.executar_calculos()
