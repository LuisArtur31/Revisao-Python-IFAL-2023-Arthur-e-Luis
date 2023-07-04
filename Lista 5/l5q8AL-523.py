#Lista de Exercício 5 - Questão 8
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

class QuantidadeDigitos:
    def __init__(self, numero):
        self.numero = numero

    def calcular_quantidade_digitos(self):
        if self.numero == 0:
            return 1

        quantidade = 0
        numero_absoluto = abs(self.numero)

        while numero_absoluto > 0:
            numero_absoluto //= 10
            quantidade += 1

        return quantidade


def main():
    try:
        numero = int(input("Digite um número inteiro: "))

        quantidade_digitos = QuantidadeDigitos(numero)
        quantidade = quantidade_digitos.calcular_quantidade_digitos()

        print(f"A quantidade de dígitos do número {numero} é: {quantidade}")

    except ValueError:
        print("Erro: O valor digitado não é um número inteiro.")


if __name__ == "__main__":
    main()
