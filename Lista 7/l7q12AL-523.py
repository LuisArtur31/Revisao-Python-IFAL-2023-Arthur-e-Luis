#Lista de Exercício 7 - Questão 12
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.

class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros

    def adicioneJuros(self):
        juros = self.saldo * (self.taxa_juros / 100)
        self.saldo += juros

    def getSaldo(self):
        return self.saldo

# Exemplo de uso da classe ContaInvestimento
conta = ContaInvestimento(1000.00, 10)

print("Saldo inicial: R$", conta.getSaldo())

for _ in range(5):
    conta.adicioneJuros()

print("Saldo após aplicar juros: R$", conta.getSaldo())
