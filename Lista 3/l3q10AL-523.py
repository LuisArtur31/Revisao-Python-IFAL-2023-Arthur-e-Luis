#Lista de Exercício 3 - Questão 10
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

class IntervaloNumerico:
    def __init__(self):
        self.numero1 = 0
        self.numero2 = 0

    def ler_numeros(self):
        while True:
            try:
                self.numero1 = int(input("Digite o primeiro número inteiro: "))
                self.numero2 = int(input("Digite o segundo número inteiro: "))
                break
            except ValueError:
                print("Valor inválido. Digite um número inteiro válido.")

    def gerar_intervalo(self):
        inicio = min(self.numero1, self.numero2)
        fim = max(self.numero1, self.numero2)

        intervalo = range(inicio, fim + 1)
        return list(intervalo)


def main():
    intervalo = IntervaloNumerico()
    intervalo.ler_numeros()

    numeros_intervalo = intervalo.gerar_intervalo()

    print("Números no intervalo:")
    for numero in numeros_intervalo:
        print(numero)


if __name__ == "__main__":
    main()
