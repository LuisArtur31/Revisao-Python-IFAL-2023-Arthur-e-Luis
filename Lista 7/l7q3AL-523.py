#Lista de Exercício 7 - Questão 3
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Retangulo: Crie uma classe que modele um retangulo:

#Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudarValorLados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornarValorLados(self):
        return self.lado_a, self.lado_b

    def calcularArea(self):
        return self.lado_a * self.lado_b

    def calcularPerimetro(self):
        return 2 * (self.lado_a + self.lado_b)


try:
    # Entrada do usuário para as medidas do local
    lado_a = float(input("Digite o valor do lado A do retângulo: "))
    lado_b = float(input("Digite o valor do lado B do retângulo: "))

    # Criação do objeto retângulo com as medidas informadas
    meu_retangulo = Retangulo(lado_a, lado_b)

    # Cálculo da quantidade de pisos e rodapés necessários
    area_total = meu_retangulo.calcularArea()
    perimetro_total = meu_retangulo.calcularPerimetro()

    area_piso = float(input("Digite o valor da área de cada piso em metros quadrados: "))
    area_rodape = float(input("Digite o valor da área de cada rodapé em metros quadrados: "))

    quantidade_pisos = area_total / area_piso
    quantidade_rodapes = perimetro_total / area_rodape

    print("Quantidade de pisos necessários:", quantidade_pisos)
    print("Quantidade de rodapés necessários:", quantidade_rodapes)

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

