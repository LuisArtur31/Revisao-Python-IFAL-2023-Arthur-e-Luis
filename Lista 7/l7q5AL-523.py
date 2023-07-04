#Lista de Exercício 7 - Questão 5
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            raise ValueError("O valor do depósito deve ser maior que zero.")

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            raise ValueError("Saldo insuficiente para o saque.")

try:
    # Criação de uma instância da classe ContaCorrente
    conta = ContaCorrente("123456", "João da Silva")

    # Alteração do nome do correntista
    novo_nome = input("Digite o novo nome do correntista: ")
    conta.alterarNome(novo_nome)

    # Realização de depósito
    valor_deposito = float(input("Digite o valor do depósito: "))
    conta.deposito(valor_deposito)

    # Realização de saque
    valor_saque = float(input("Digite o valor do saque: "))
    conta.saque(valor_saque)

    print("Dados da conta corrente:")
    print("Número da conta:", conta.numero_conta)
    print("Nome do correntista:", conta.nome_correntista)
    print("Saldo:", conta.saldo)

except ValueError as e:
    print("Ocorreu um erro:", str(e))

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
