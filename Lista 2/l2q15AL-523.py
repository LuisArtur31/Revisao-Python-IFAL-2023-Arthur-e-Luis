#Lista de Exercício 2 - Questão 15
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def verificar_triangulo(self):
        if self.lado1 + self.lado2 > self.lado3 and self.lado1 + self.lado3 > self.lado2 and self.lado2 + self.lado3 > self.lado1:
            return True
        else:
            return False

    def obter_tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"


try:
    lado1 = float(input("Digite o primeiro lado do triângulo: "))
    lado2 = float(input("Digite o segundo lado do triângulo: "))
    lado3 = float(input("Digite o terceiro lado do triângulo: "))

    triangulo = Triangulo(lado1, lado2, lado3)

    if triangulo.verificar_triangulo():
        tipo_triangulo = triangulo.obter_tipo_triangulo()
        print(f"Os lados fornecidos formam um triângulo {tipo_triangulo}.")
    else:
        print("Os lados fornecidos não podem formar um triângulo.")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar números válidos para os lados do triângulo.")
