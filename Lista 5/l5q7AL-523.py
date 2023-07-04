#Lista de Exercício 5 - Questão 7
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

class Pagamento:
    def __init__(self, valor, dias_atraso):
        self.valor = valor
        self.dias_atraso = dias_atraso

    def calcular_valor_pagamento(self):
        valor_total = self.valor

        if self.dias_atraso > 0:
            multa = self.valor * 0.03
            juros = self.valor * (0.001 * self.dias_atraso)
            valor_total = self.valor + multa + juros

        return valor_total


def main():
    prestacoes_pagas = 0
    valor_total_pagamento = 0

    try:
        while True:
            valor_prestacao = float(input("Digite o valor da prestação (ou 0 para encerrar): "))

            if valor_prestacao == 0:
                break

            dias_atraso = int(input("Digite o número de dias em atraso: "))

            if dias_atraso < 0:
                raise ValueError("O número de dias em atraso deve ser um valor não negativo.")

            pagamento = Pagamento(valor_prestacao, dias_atraso)
            valor_a_pagar = pagamento.calcular_valor_pagamento()

            print(f"Valor a ser pago: R${valor_a_pagar:.2f}")

            prestacoes_pagas += 1
            valor_total_pagamento += valor_a_pagar

    except ValueError as error:
        print(f"Erro: {str(error)}")

    finally:
        print("\nRelatório do dia:")
        print(f"Quantidade de prestações pagas: {prestacoes_pagas}")
        print(f"Valor total pago: R${valor_total_pagamento:.2f}")


if __name__ == "__main__":
    main()
