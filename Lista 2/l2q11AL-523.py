#Lista de Exercício 2 - Questão 11
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

class Colaborador:
    def __init__(self, salario):
        self.salario = salario
    
    def calcular_reajuste(self):
        reajuste = 0
        if self.salario <= 280:
            reajuste = 0.2
        elif self.salario <= 700:
            reajuste = 0.15
        elif self.salario <= 1500:
            reajuste = 0.1
        else:
            reajuste = 0.05
        
        aumento = self.salario * reajuste
        novo_salario = self.salario + aumento
        
        return aumento, novo_salario
    
try:
    salario = float(input("Digite o salário do colaborador: R$ "))
    colaborador = Colaborador(salario)
    aumento, novo_salario = colaborador.calcular_reajuste()
    
    print("Salário antes do reajuste: R$ {:.2f}".format(salario))
    print("Percentual de aumento aplicado: {:.2f}%".format(aumento * 100 / salario))
    print("Valor do aumento: R$ {:.2f}".format(aumento))
    print("Novo salário após o aumento: R$ {:.2f}".format(novo_salario))

except ValueError:
    print("Erro: valor inválido. Certifique-se de digitar um número válido.")
