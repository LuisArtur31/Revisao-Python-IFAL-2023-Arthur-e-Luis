#Lista de Exercício 3 - Questão 42
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

class Intervalo:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        self.contagem = 0


def contar_numeros():
    intervalos = [
        Intervalo(0, 25),
        Intervalo(26, 50),
        Intervalo(51, 75),
        Intervalo(76, 100)
    ]

    while True:
        numero = int(input("Digite um número positivo (ou negativo para sair): "))
        if numero < 0:
            break

        for intervalo in intervalos:
            if intervalo.inicio <= numero <= intervalo.fim:
                intervalo.contagem += 1

    return intervalos


def main():
    try:
        intervalos = contar_numeros()

        print("\nResultados:")
        for intervalo in intervalos:
            print("Quantidade de números no intervalo [{}, {}]: {}".format(
                intervalo.inicio, intervalo.fim, intervalo.contagem
            ))

    except ValueError as e:
        print("Erro: {}".format(e))


if __name__ == "__main__":
    main()
