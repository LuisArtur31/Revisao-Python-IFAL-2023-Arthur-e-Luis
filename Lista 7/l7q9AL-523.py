#Lista de Exercício 7 - Questão 9
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

#Possua uma classe chamada Ponto, com os atributos x e y.
#Possua uma classe chamada Retangulo, com os atributos largura e altura.
#Possua uma função para imprimir os valores da classe Ponto
#Possua uma função para encontrar o centro de um Retângulo.
#Você deve criar alguns objetos da classe Retangulo.
#ada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
#A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
#O valor do centro do objeto deve ser mostrado na tela
#Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Coordenadas do ponto: ({self.x}, {self.y})")


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        centro = Ponto(centro_x, centro_y)
        return centro


def alterar_retangulo(retangulo):
    x = float(input("Digite a coordenada x do ponto inicial: "))
    y = float(input("Digite a coordenada y do ponto inicial: "))
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))

    ponto_inicial = Ponto(x, y)
    retangulo.ponto_inicial = ponto_inicial
    retangulo.largura = largura
    retangulo.altura = altura


def imprimir_centro(retangulo):
    centro = retangulo.encontrar_centro()
    centro.imprimir()


# Programa principal
retangulo = Retangulo(Ponto(0, 0), 5, 3)

while True:
    print("\n=== Menu ===")
    print("1. Alterar retângulo")
    print("2. Imprimir centro do retângulo")
    print("0. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        alterar_retangulo(retangulo)
    elif opcao == "2":
        imprimir_centro(retangulo)
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Digite novamente.")

