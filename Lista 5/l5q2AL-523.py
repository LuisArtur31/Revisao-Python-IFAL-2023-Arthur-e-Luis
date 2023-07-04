#Lista de Exercício 5 - Questão 2
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa para imprimir:
#    1
#    1   2
#    1   2   3
#    .....
#    1   2   3   ...  n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

class SequenciaNumerica:
    def __init__(self, n):
        self.n = n
    
    def imprimir(self):
        for i in range(1, self.n + 1):
            linha = [str(j) for j in range(1, i + 1)]
            print("   ".join(linha))

try:
    n = int(input("Digite um número inteiro: "))
    padrao = SequenciaNumerica(n)
    padrao.imprimir()
except ValueError:
    print("Entrada inválida. Digite um número inteiro.")
