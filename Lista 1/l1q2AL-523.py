#Lista de Exercício 1 - Questão 2
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça um número e então mostre a mensagem "O número informado foi [número]."

class NumeroInvalidoException(Exception):
    pass


class Calculadora:
    def __init__(self):
        self.numero = None

    def ler_numero(self):
        try:
            self.numero = float(input("Digite um número: "))
        except ValueError:
            raise NumeroInvalidoException("Número inválido. Tente novamente.")

    def exibir_numero(self):
        if self.numero is None:
            raise NumeroInvalidoException("Nenhum número foi informado.")
        else:
            print(f"O número informado foi {self.numero}.")


def main():
    calculadora = Calculadora()

    try:
        calculadora.ler_numero()
        calculadora.exibir_numero()
    except NumeroInvalidoException as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
