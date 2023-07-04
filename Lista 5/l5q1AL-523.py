#Lista de Exercício 5 - Questão 1
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

class PadraoNumerico:
    def __init__(self, n):
        self.n = n

    def imprimir_padrao(self):
        for i in range(1, self.n + 1):
            linha = " ".join(str(i) for _ in range(i))
            print(linha)

def main():
    try:
        n = int(input("Digite um valor para n: "))
        if n <= 0:
            raise ValueError("O valor de n deve ser maior que zero.")

        padrao = PadraoNumerico(n)
        padrao.imprimir_padrao()

    except ValueError as error:
        print("Erro:", str(error))

if __name__ == "__main__":
    main()




