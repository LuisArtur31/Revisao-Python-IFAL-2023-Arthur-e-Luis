#Lista de Exercício 2 - Questão 22
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

class NumeroInvalidoException(Exception):
    pass


class VerificadorParImpar:
    def __init__(self, numero):
        self.numero = numero

    def verificar_par_impar(self):
        if not isinstance(self.numero, int):
            raise NumeroInvalidoException("O valor fornecido não é um número inteiro.")

        if self.numero % 2 == 0:
            return "par"
        else:
            return "ímpar"


def main():
    try:
        numero = int(input("Digite um número inteiro: "))

        verificador = VerificadorParImpar(numero)
        resultado = verificador.verificar_par_impar()
        print(f"O número é {resultado}.")
    except (ValueError, NumeroInvalidoException) as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
