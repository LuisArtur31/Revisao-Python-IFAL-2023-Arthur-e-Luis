#Lista de Exercício 7 - Questão 4
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Pessoa: Crie uma classe que modele uma pessoa:
#Atributos: nome, idade, peso e altura
#Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome  # Atributo privado para encapsulamento
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def envelhecer(self, anos):
        if anos > 0:
            self.__idade += anos
            if self.__idade < 21:
                self.__altura += 0.5 * anos
        else:
            raise ValueError("O número de anos deve ser positivo.")

    def engordar(self, quilos):
        if quilos > 0:
            self.__peso += quilos
        else:
            raise ValueError("O número de quilos deve ser positivo.")

    def emagrecer(self, quilos):
        if quilos > 0 and quilos <= self.__peso:
            self.__peso -= quilos
        else:
            raise ValueError("O número de quilos deve ser positivo e não pode exceder o peso atual.")

    def crescer(self, altura):
        if altura > 0:
            self.__altura += altura
        else:
            raise ValueError("A altura deve ser positiva.")

    def retornar_dados(self):
        return f"Nome: {self.__nome}, Idade: {self.__idade} anos, Peso: {self.__peso} kg, Altura: {self.__altura} cm"


# Exemplo de uso:
try:
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    peso = float(input("Digite o peso da pessoa (em kg): "))
    altura = float(input("Digite a altura da pessoa (em cm): "))

    pessoa = Pessoa(nome, idade, peso, altura)
    print("Dados iniciais:", pessoa.retornar_dados())

    anos_envelhecer = int(input("Digite quantos anos a pessoa deve envelhecer: "))
    pessoa.envelhecer(anos_envelhecer)
    print("Dados após envelhecer:", pessoa.retornar_dados())

    quilos_engordar = float(input("Digite quantos quilos a pessoa deve engordar: "))
    pessoa.engordar(quilos_engordar)
    print("Dados após engordar:", pessoa.retornar_dados())

    quilos_emagrecer = float(input("Digite quantos quilos a pessoa deve emagrecer: "))
    pessoa.emagrecer(quilos_emagrecer)
    print("Dados após emagrecer:", pessoa.retornar_dados())

    altura_crescer = float(input("Digite quantos centímetros a pessoa deve crescer: "))
    pessoa.crescer(altura_crescer)
    print("Dados após crescer:", pessoa.retornar_dados())

except ValueError as e:
    print("Erro:", str(e))
