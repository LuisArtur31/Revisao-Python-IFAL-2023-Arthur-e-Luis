#Lista de Exercício 7 - Questão 7
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

#Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.

class BichinhoVirtual:
    def __init__(self, nome, fome=0, saude=100, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, novo_valor):
        if novo_valor >= 0:
            self.fome = novo_valor
        else:
            raise ValueError("O valor da fome não pode ser negativo.")

    def alterarSaude(self, novo_valor):
        if novo_valor >= 0:
            self.saude = novo_valor
        else:
            raise ValueError("O valor da saúde não pode ser negativo.")

    def alterarIdade(self, novo_valor):
        if novo_valor >= 0:
            self.idade = novo_valor
        else:
            raise ValueError("O valor da idade não pode ser negativo.")

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

    def retornarHumor(self):
        return self.fome + self.saude

try:
    # Criação de uma instância da classe BichinhoVirtual
    bichinho = BichinhoVirtual("Meu Tamagushi")

    # Alteração dos atributos do bichinho
    bichinho.alterarNome("Novo Nome")
    bichinho.alterarFome(50)
    bichinho.alterarSaude(80)
    bichinho.alterarIdade(2)

    # Exibição dos atributos do bichinho
    print("Nome:", bichinho.retornarNome())
    print("Fome:", bichinho.retornarFome())
    print("Saúde:", bichinho.retornarSaude())
    print("Idade:", bichinho.retornarIdade())
    print("Humor:", bichinho.retornarHumor())

except ValueError as e:
    print("Ocorreu um erro:", str(e))

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
