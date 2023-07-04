#Lista de Exercício 5 - Questão 9
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

class ReversoNumero:
    def __init__(self, numero):
        self.numero = numero

    def calcular_reverso(self):
        numero_absoluto = abs(self.numero)
        reverso = int(str(numero_absoluto)[::-1])

        if self.numero < 0:
            reverso *= -1

        return reverso


def main():
    try:
        numero = int(input("Digite um número inteiro: "))

        reverso_numero = ReversoNumero(numero)
        reverso = reverso_numero.calcular_reverso()

        print(f"O reverso do número {numero} é: {reverso}")

    except ValueError:
        print("Erro: O valor digitado não é um número inteiro.")


if __name__ == "__main__":
    main()
