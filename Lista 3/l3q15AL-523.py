#Lista de Exercício 3 - Questão 15
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

class serieFibonacci:
    def __init__(self):
        self.termos = []

    def gerarFibonacci(self, n):
        a, b = 0, 1
        for _ in range(n):
            self.termos.append(a)
            a, b = b, a + b

    def exibirFibonacci(self):
        for termo in self.termos:
            print(termo, end=" ")
        print()

    def ler_n(self):
        while True:
            try:
                n = int(input("Digite o valor de n: "))
                if n < 1:
                    print("Valor inválido. Digite um número maior ou igual a 1.")
                else:
                    return n
            except ValueError:
                print("Valor inválido. Digite um número inteiro válido.")


def main():
    fibonacci = serieFibonacci()
    n = fibonacci.ler_n()
    fibonacci.gerarFibonacci(n)
    fibonacci.exibirFibonacci()


if __name__ == "__main__":
    main()
