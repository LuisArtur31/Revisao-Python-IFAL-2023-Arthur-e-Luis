#Lista de Exercício 2 - Questão 12
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00


class ValorInvalidoException(Exception):
    pass


class FolhaPagamento:
    def __init__(self, valor_hora, horas_trabalhadas):
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_salario_bruto(self):
        salario_bruto = self.valor_hora * self.horas_trabalhadas
        return salario_bruto

    def calcular_ir(self, salario_bruto):
        if salario_bruto <= 900:
            ir = 0
        elif salario_bruto <= 1500:
            ir = salario_bruto * 0.05
        elif salario_bruto <= 2500:
            ir = salario_bruto * 0.1
        else:
            ir = salario_bruto * 0.2
        return ir

    def calcular_inss(self, salario_bruto):
        inss = salario_bruto * 0.1
        return inss

    def calcular_fgts(self, salario_bruto):
        fgts = salario_bruto * 0.11
        return fgts

    def calcular_salario_liquido(self, salario_bruto, ir, inss):
        salario_liquido = salario_bruto - ir - inss
        return salario_liquido

    def imprimir_folha_pagamento(self):
        salario_bruto = self.calcular_salario_bruto()
        ir = self.calcular_ir(salario_bruto)
        inss = self.calcular_inss(salario_bruto)
        fgts = self.calcular_fgts(salario_bruto)
        total_descontos = ir + inss
        salario_liquido = self.calcular_salario_liquido(salario_bruto, ir, inss)

        print("Folha de Pagamento")
        print(f"Salário Bruto: R${salario_bruto:.2f}")
        print(f"(-) IR: R${ir:.2f}")
        print(f"(-) INSS: R${inss:.2f}")
        print(f"FGTS: R${fgts:.2f}")
        print(f"Total de descontos: R${total_descontos:.2f}")
        print(f"Salário Líquido: R${salario_liquido:.2f}")


def main():
    try:
        valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
        horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

        if valor_hora < 0 or horas_trabalhadas < 0:
            raise ValorInvalidoException("Valor inválido. Os valores devem ser positivos.")

        folha_pagamento = FolhaPagamento(valor_hora, horas_trabalhadas)
        folha_pagamento.imprimir_folha_pagamento()
    except ValueError:
        print("Valor inválido. Digite um número.")
    except ValorInvalidoException as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
