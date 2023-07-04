#Lista de Exercício 7 - Questão 15
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.

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
            self.saude += tempo_brincadeira
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

try:
    # Criação de uma instância da classe BichinhoVirtual
    bichinho = BichinhoVirtual("Meu Tamagushi")

    # Alteração dos atributos do bichinho
    bichinho.alterarNome("Novo Nome")

    quantidade_comida = int(input("Digite a quantidade de comida fornecida: "))
    tempo_brincadeira = int(input("Digite o tempo de brincadeira: "))

    bichinho.alterarFome(quantidade_comida)
    bichinho.alterarSaude(tempo_brincadeira)

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
