#Lista de Exercício 3 - Questão 38
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

class Funcionario:
    def __init__(self, salario_inicial):
        self.salario_inicial = salario_inicial

    def calcular_salario_atual(self):
        try:
            percentual_aumento = 0.015  # 1,5% de aumento em 1996
            salario_atual = self.salario_inicial

            for ano in range(1997, 2023):  # Aumentos a partir de 1997 até 2022 (inclusive)
                salario_atual += salario_atual * percentual_aumento
                percentual_aumento *= 2  # Dobrando o percentual de aumento para o próximo ano

            return salario_atual

        except Exception as e:
            raise ValueError("Entrada inválida: {}".format(e))


def main():
    try:
        salario_inicial = float(input("Digite o salário inicial do funcionário: "))
        funcionario = Funcionario(salario_inicial)
        salario_atual = funcionario.calcular_salario_atual()
        print("O salário atual do funcionário é R$ {:.2f}".format(salario_atual))

    except ValueError as e:
        print("Erro: {}".format(e))


if __name__ == "__main__":
    main()
