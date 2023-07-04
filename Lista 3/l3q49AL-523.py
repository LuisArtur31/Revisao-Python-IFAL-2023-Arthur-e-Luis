#Lista de Exercício 3 - Questão 49
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que mostre os n termos da Série a seguir:
#  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
#Imprima no final a soma da série.

class Serie:
    def __init__(self, n):
        self.n = n

    def calcular_serie(self):
        soma = 0
        denominador = 1

        for i in range(1, self.n+1):
            termo = i / denominador
            soma += termo
            denominador += 2

        return soma


def main():
    while True:
        try:
            n = int(input("Digite o número de termos da série: "))
            if n < 1:
                raise ValueError
            break
        except ValueError:
            print("Valor inválido. Digite um número inteiro positivo.")

    serie = Serie(n)
    soma = serie.calcular_serie()

    print("Termos da série:")
    denominador = 1
    for i in range(1, n+1):
        termo = i / denominador
        print(f"{i}/{denominador} = {termo}")
        denominador += 2

    print(f"\nSoma da série: {soma}")


if __name__ == "__main__":
    main()
