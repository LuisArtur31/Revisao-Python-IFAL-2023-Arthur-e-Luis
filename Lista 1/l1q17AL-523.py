#Lista de Exercício 1 - Questão 17
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

class LojaDeTintas:
    def __init__(self, area_a_ser_pintada):
        self.area_a_ser_pintada = area_a_ser_pintada
    
    def calcular_quantidade_latas(self):
        quantidade_litros = math.ceil((self.area_a_ser_pintada * 1.1) / 6)  # Considerando 10% de folga
        quantidade_latas = math.ceil(quantidade_litros / 18)
        return quantidade_latas
    
    def calcular_preco_latas(self):
        quantidade_latas = self.calcular_quantidade_latas()
        preco_total = quantidade_latas * 80.00
        return preco_total
    
    def calcular_quantidade_galoes(self):
        quantidade_litros = math.ceil((self.area_a_ser_pintada * 1.1) / 6)  # Considerando 10% de folga
        quantidade_galoes = math.ceil(quantidade_litros / 3.6)
        return quantidade_galoes
    
    def calcular_preco_galoes(self):
        quantidade_galoes = self.calcular_quantidade_galoes()
        preco_total = quantidade_galoes * 25.00
        return preco_total
    
    def calcular_mistura(self):
        quantidade_litros = math.ceil((self.area_a_ser_pintada * 1.1) / 6)  # Considerando 10% de folga
        quantidade_latas = quantidade_litros // 18
        quantidade_galoes = math.ceil((quantidade_litros % 18) / 3.6)
        
        preco_total = (quantidade_latas * 80.00) + (quantidade_galoes * 25.00)
        return quantidade_latas, quantidade_galoes, preco_total


def solicitar_area():
    while True:
        try:
            area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
            if area <= 0:
                print("Digite um valor válido para a área.")
            else:
                return area
        except ValueError:
            print("Digite um valor numérico para a área.")

def imprimir_resultado(quantidade, preco):
    print("Quantidade de tinta:", quantidade)
    print("Preço total: R$", preco)


try:
    area_pintada = solicitar_area()

    loja_tintas = LojaDeTintas(area_pintada)

    print("\nSituação 1: Comprar apenas latas de 18 litros")
    quantidade_latas = loja_tintas.calcular_quantidade_latas()
    preco_latas = loja_tintas.calcular_preco_latas()
    imprimir_resultado(quantidade_latas, preco_latas)

    print("\nSituação 2: Comprar apenas galões de 3,6 litros")
    quantidade_galoes = loja_tintas.calcular_quantidade_galoes()
    preco_galoes = loja_tintas.calcular_preco_galoes()
    imprimir_resultado(quantidade_galoes, preco_galoes)

    print("\nSituação 3: Misturar latas e galões")
    quantidade_latas, quantidade_galoes, preco_total = loja_tintas.calcular_mistura()
    print("Quantidade de latas:", quantidade_latas)
    print("Quantidade de galões:", quantidade_galoes)
    print("Preço total: R$", preco_total)

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
