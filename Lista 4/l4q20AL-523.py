#Lista de Exercício 4 - Questão 20
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
#Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
#a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
#*O salário de cada funcionário, juntamente com o valor do abono;
#*O número total de funcionário processados;
#*O valor total a ser gasto com o pagamento do abono;
#*O número de funcionário que receberá o valor mínimo de 100 reais;
#*O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.
#Projeção de Gastos com Abono
#============================ 
 
#Salário: 1000
#Salário: 300
#Salário: 500
#Salário: 100
#Salário: 4500
#Salário: 0
 
#Salário    - Abono     
#R$ 1000.00 - R$  200.00
#R$  300.00 - R$  100.00
#R$  500.00 - R$  100.00
#R$  100.00 - R$  100.00
#R$ 4500.00 - R$  900.00

#Foram processados 5 colaboradores
#Total gasto com abonos: R$ 1400.00
#Valor mínimo pago a 3 colaboradores
#Maior valor de abono pago: R$ 900.00

class Colaborador:
    def __init__(self, salario):
        self.salario = salario
        self.abono = self.calcular_abono()

    def calcular_abono(self):
        if self.salario <= 0:
            return 0
        elif self.salario * 0.2 < 100:
            return 100
        else:
            return self.salario * 0.2


def obter_salario():
    while True:
        try:
            salario = float(input("Salário (ou digite 0 para obter os resultados): "))
            if salario >= 0:
                return salario
            else:
                print("Valor inválido. Digite um salário não negativo.")
        except ValueError:
            print("Valor inválido. Digite um número válido.")


def main():
    colaboradores = []
    salario = obter_salario()

    while salario != 0:
        colaborador = Colaborador(salario)
        colaboradores.append(colaborador)
        salario = obter_salario()

    total_colaboradores = len(colaboradores)
    total_abonos = sum(colaborador.abono for colaborador in colaboradores)
    min_abono = sum(colaborador.abono == 100 for colaborador in colaboradores)
    max_abono = max(colaborador.abono for colaborador in colaboradores)

    print("\nProjeção de Gastos com Abono")
    print("============================\n")
    print("Salário    - Abono")
    for colaborador in colaboradores:
        print(f"R$ {colaborador.salario:.2f} - R$ {colaborador.abono:.2f}")
    print("\n")

    print(f"Foram processados {total_colaboradores} colaboradores")
    print(f"Total gasto com abonos: R$ {total_abonos:.2f}")
    print(f"Valor mínimo pago a {min_abono} colaboradores")
    print(f"Maior valor de abono pago: R$ {max_abono:.2f}")


if __name__ == "__main__":
    main()
