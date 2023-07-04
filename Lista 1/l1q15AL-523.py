#Lista de Exercício 1 - Questão 15
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

class Salario:
    def __init__(self, valor_hora, horas_trabalhadas):
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_salario_bruto(self):
        return self.valor_hora * self.horas_trabalhadas

    def calcular_desconto_ir(self, salario_bruto):
        return salario_bruto * 0.11

    def calcular_desconto_inss(self, salario_bruto):
        return salario_bruto * 0.08

    def calcular_desconto_sindicato(self, salario_bruto):
        return salario_bruto * 0.05

    def calcular_salario_liquido(self, salario_bruto):
        desconto_ir = self.calcular_desconto_ir(salario_bruto)
        desconto_inss = self.calcular_desconto_inss(salario_bruto)
        desconto_sindicato = self.calcular_desconto_sindicato(salario_bruto)

        salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato
        return salario_liquido


def ler_valor_hora():
    try:
        valor_hora = float(input("Digite o valor ganho por hora: "))
        return valor_hora
    except ValueError:
        print("Erro: Digite um valor válido.")
        return ler_valor_hora()


def ler_horas_trabalhadas():
    try:
        horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
        return horas_trabalhadas
    except ValueError:
        print("Erro: Digite um número válido.")
        return ler_horas_trabalhadas()


try:
    valor_hora = ler_valor_hora()
    horas_trabalhadas = ler_horas_trabalhadas()

    salario = Salario(valor_hora, horas_trabalhadas)
    salario_bruto = salario.calcular_salario_bruto()
    desconto_ir = salario.calcular_desconto_ir(salario_bruto)
    desconto_inss = salario.calcular_desconto_inss(salario_bruto)
    desconto_sindicato = salario.calcular_desconto_sindicato(salario_bruto)
    salario_liquido = salario.calcular_salario_liquido(salario_bruto)

    print(f"Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"Desconto IR (11%): R$ {desconto_ir:.2f}")
    print(f"Desconto INSS (8%): R$ {desconto_inss:.2f}")
    print(f"Desconto Sindicato (5%): R$ {desconto_sindicato:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

except ValueError as error:
    print(f"Erro: {str(error)}")
