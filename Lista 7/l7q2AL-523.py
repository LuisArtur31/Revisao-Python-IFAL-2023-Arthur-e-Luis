#Lista de Exercício 7 - Questão 2
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Quadrado: Crie uma classe que modele um quadrado:
#Atributos: Tamanho do lado
#Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área.

class Quadrado:
    def __init__(self, lado):
        self.__lado = lado  # Atributo privado para encapsulamento

    def mudar_lado(self, novo_lado):
        if novo_lado > 0:
            self.__lado = novo_lado
        else:
            raise ValueError("O lado do quadrado deve ser maior que zero.")

    def retornar_lado(self):
        return self.__lado

    def calcular_area(self):
        return self.__lado ** 2


# Exemplo de uso:
try:
    lado_quadrado = float(input("Digite o tamanho do lado do quadrado: "))
    meu_quadrado = Quadrado(lado_quadrado)
    print("Lado do quadrado:", meu_quadrado.retornar_lado())
    print("Área do quadrado:", meu_quadrado.calcular_area())

    novo_lado = float(input("Digite o novo tamanho do lado do quadrado: "))
    meu_quadrado.mudar_lado(novo_lado)
    print("Novo lado do quadrado:", meu_quadrado.retornar_lado())
    print("Nova área do quadrado:", meu_quadrado.calcular_area())

except ValueError as e:
    print("Erro:", str(e))
