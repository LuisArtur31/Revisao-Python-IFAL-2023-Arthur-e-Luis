#Lista de Exercício 1 - Questão 8
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

class ValorInvalidoException(Exception):
    pass


class CalculadoraSalario:
    def __init__(self):
        self.valor_hora = None
        self.horas_trabalhadas = None

    def ler_dados(self):
        while True:
            try:
                self.valor_hora = float(input("Digite o valor que você ganha por hora: "))
                if self.valor_hora < 0:
                    raise ValorInvalidoException("Valor inválido. Digite um valor positivo.")
                break
            except ValueError:
                print("Valor inválido. Digite um número.")
            except ValorInvalidoException as e:
                print(f"Erro: {str(e)}")

        while True:
            try:
                self.horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
                if self.horas_trabalhadas < 0:
                    raise ValorInvalidoException("Valor inválido. Digite um valor positivo.")
                break
            except ValueError:
                print("Valor inválido. Digite um número.")
            except ValorInvalidoException as e:
                print(f"Erro: {str(e)}")

    def calcular_salario(self):
        if self.valor_hora is None or self.horas_trabalhadas is None:
            raise ValorInvalidoException("Os dados estão incompletos.")

        salario = self.valor_hora * self.horas_trabalhadas
        return salario


def main():
    calculadora = CalculadoraSalario()

    try:
        calculadora.ler_dados()
        salario = calculadora.calcular_salario()
        print(f"O total do seu salário no mês é: R$ {salario:.2f}")
    except ValorInvalidoException as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
