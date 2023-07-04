#Lista de Exercício 7 - Questão 16
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.

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

    def __str__(self):
        return f"Nome: {self.nome}\nFome: {self.fome}\nSaúde: {self.saude}\nIdade: {self.idade}"

try:
    # Criação de uma instância da classe BichinhoVirtual
    bichinho = BichinhoVirtual("Meu Tamagushi")

    while True:
        print("\n--- Menu ---")
        print("1. Alterar nome")
        print("2. Alterar fome")
        print("3. Alterar saúde")
        print("4. Alterar idade")
        print("5. Exibir humor")
        print("6. Opção secreta")
        print("0. Sair")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            novo_nome = input("Digite o novo nome: ")
            bichinho.alterarNome(novo_nome)
        elif escolha == 2:
            novo_valor = int(input("Digite o novo valor de fome: "))
            bichinho.alterarFome(novo_valor)
        elif escolha == 3:
            novo_valor = int(input("Digite o novo valor de saúde: "))
            bichinho.alterarSaude(novo_valor)
        elif escolha == 4:
            novo_valor = int(input("Digite o novo valor de idade: "))
            bichinho.alterarIdade(novo_valor)
        elif escolha == 5:
            print("Humor:", bichinho.retornarHumor())
        elif escolha == 6:
            print("Opção secreta selecionada!")
            print(bichinho)  # Exibe os valores exatos dos atributos do objeto
        elif escolha == 0:
            break
        else:
            print("Opção inválida!")

except ValueError as e:
    print("Ocorreu um erro:", str(e))

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
