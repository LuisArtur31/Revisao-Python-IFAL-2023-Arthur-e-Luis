#Lista de Exercício 7 - Questão 14
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
#Exemplo de uso:
#  harry=funcionário("Harry",25000)
#  harry.aumentarSalario(10)

class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros

    def adicioneJuros(self):
        juros = self.saldo * (self.taxa_juros / 100)
        self.saldo += juros

    def getSaldo(self):
        return self.saldo

    def aumentarSalario(self, porcentualDeAumento):
        if porcentualDeAumento < 0:
            raise ValueError("O porcentual de aumento deve ser um valor positivo.")
        
        aumento = self.saldo * (porcentualDeAumento / 100)
        self.saldo += aumento

# Exemplo de uso da classe ContaInvestimento
conta = ContaInvestimento(1000.00, 10)

print("Saldo inicial: R$", conta.getSaldo())

for _ in range(5):
    conta.adicioneJuros()

print("Saldo após aplicar juros: R$", conta.getSaldo())

conta.aumentarSalario(10)

print("Saldo após aumentar o salário: R$", conta.getSaldo())

# Criando uma pessoa chamada "Arthur" com saldo inicial de 5000
pessoa = ContaInvestimento(5000, 0)

print("Saldo inicial: R$", pessoa.getSaldo())

# Aplicando juros
pessoa.adicioneJuros()

print("Saldo após aplicar juros: R$", pessoa.getSaldo())

# Aumentando o salário em 10%
pessoa.aumentarSalario(10)

print("Saldo após aumentar o salário: R$", pessoa.getSaldo())
