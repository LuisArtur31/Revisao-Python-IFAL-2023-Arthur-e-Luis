#Lista de Exercício 7 - Questão 17
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.

import random

class BichinhoVirtual:
    def __init__(self, nome, fome=0, saude=100, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, quantidade_comida):
        if quantidade_comida >= 0:
            self.fome -= quantidade_comida
        else:
            raise ValueError("A quantidade de comida não pode ser negativa.")

    def alterarSaude(self, tempo_brincadeira):
        if tempo_brincadeira >= 0:
            self.saude -= tempo_brincadeira
        else:
            raise ValueError("O tempo de brincadeira não pode ser negativo.")

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

    def __str__(self):
        return f"Bichinho: {self.nome}\nFome: {self.fome}\nSaúde: {self.saude}\nIdade: {self.idade}\n"

class FazendaDeBichinhos:
    def __init__(self):
        self.bichinhos = []

    def adicionarBichinho(self, bichinho):
        self.bichinhos.append(bichinho)

    def alimentarBichinhos(self, quantidade_comida):
        for bichinho in self.bichinhos:
            bichinho.alterarFome(quantidade_comida)

    def brincarComBichinhos(self, tempo_brincadeira):
        for bichinho in self.bichinhos:
            bichinho.alterarSaude(tempo_brincadeira)

    def ouvirBichinhos(self):
        for bichinho in self.bichinhos:
            print(bichinho)

    def executarAcao(self, opcao):
        if opcao == 1:
            quantidade_comida = int(input("Digite a quantidade de comida fornecida: "))
            self.alimentarBichinhos(quantidade_comida)
        elif opcao == 2:
            tempo_brincadeira = int(input("Digite o tempo de brincadeira: "))
            self.brincarComBichinhos(tempo_brincadeira)
        elif opcao == 3:
            self.ouvirBichinhos()
        else:
            raise ValueError("Opção inválida.")

try:
    fazenda = FazendaDeBichinhos()

    # Criação de bichinhos com níveis iniciais aleatórios de fome e tédio
    nomes_bichinhos = ["Bichinho1", "Bichinho2", "Bichinho3"]
    for nome in nomes_bichinhos:
        fome_inicial = random.randint(0, 100)
        saude_inicial = random.randint(0, 100)
        idade_inicial = random.randint(0, 10)
        bichinho = BichinhoVirtual(nome, fome_inicial, saude_inicial, idade_inicial)
        fazenda.adicionarBichinho(bichinho)

    while True:
        print("----- Menu -----")
        print("1 - Alimentar bichinhos")
        print("2 - Brincar com bichinhos")
        print("3 - Ouvir bichinhos")
        print("0 - Sair")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 0:
            break

        fazenda.executarAcao(opcao)

except ValueError as e:
    print("Ocorreu um erro:", str(e))

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
