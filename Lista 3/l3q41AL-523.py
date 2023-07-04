#Lista de Exercício 3 - Questão 41
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#Os juros e a quantidade de parcelas seguem a tabela abaixo:
#Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#1       0
#3       10
#6       15
#9       20
#12      25
#Exemplo de saída do programa:
#Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
#R$ 1.000,00     0               1                       R$  1.000,00
#R$ 1.100,00     100             3                       R$    366,00
#R$ 1.150,00     150             6                       R$    191,67

class Divida:
    def __init__(self, valor_divida, juros, parcelas):
        self.valor_divida = valor_divida
        self.juros = juros
        self.parcelas = parcelas
        self.valor_juros = self.calcular_valor_juros()
        self.valor_total = self.calcular_valor_total()
        self.valor_parcela = self.calcular_valor_parcela()

    def calcular_valor_juros(self):
        return self.valor_divida * (self.juros / 100)

    def calcular_valor_total(self):
        return self.valor_divida + self.valor_juros

    def calcular_valor_parcela(self):
        return self.valor_total / self.parcelas

    def exibir_tabela(self):
        print("Valor da Dívida\tValor dos Juros\tQuantidade de Parcelas\tValor da Parcela")
        print(f"R$ {self.valor_divida:.2f}\t\tR$ {self.valor_juros:.2f}\t\t\t{self.parcelas}\t\t\tR$ {self.valor_parcela:.2f}")


def main():
    try:
        valor_divida = float(input("Digite o valor da dívida: R$ "))
        juros = float(input("Digite o valor dos juros (%): "))
        parcelas = int(input("Digite a quantidade de parcelas: "))

        divida = Divida(valor_divida, juros, parcelas)
        divida.exibir_tabela()

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar valores numéricos corretos.")


if __name__ == "__main__":
    main()
