#Lista de Exercício 2 - Questão 24
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#a - par ou ímpar;
#b - positivo ou negativo;
#c - inteiro ou decimal.

class NumeroInvalidoException(Exception):
    pass


class VerificadorNumero:
    def __init__(self, numero):
        self.numero = numero

    def verificar_par_impar(self):
        if self.numero % 2 == 0:
            return "par"
        else:
            return "ímpar"

    def verificar_positivo_negativo(self):
        if self.numero > 0:
            return "positivo"
        elif self.numero < 0:
            return "negativo"
        else:
            return "zero"

    def verificar_inteiro_decimal(self):
        if isinstance(self.numero, int):
            return "inteiro"
        else:
            return "decimal"


def main():
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        operacao = input("Digite a operação desejada (+, -, *, /): ")

        if operacao not in ["+", "-", "*", "/"]:
            raise NumeroInvalidoException("Operação inválida.")

        if operacao == "+":
            resultado = numero1 + numero2
        elif operacao == "-":
            resultado = numero1 - numero2
        elif operacao == "*":
            resultado = numero1 * numero2
        else:
            resultado = numero1 / numero2

        verificador = VerificadorNumero(resultado)
        par_impar = verificador.verificar_par_impar()
        positivo_negativo = verificador.verificar_positivo_negativo()
        inteiro_decimal = verificador.verificar_inteiro_decimal()

        print(f"O resultado da operação é: {resultado}")
        print(f"O resultado é {par_impar}, {positivo_negativo} e {inteiro_decimal}.")
    except (ValueError, ZeroDivisionError, NumeroInvalidoException) as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
