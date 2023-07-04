#Lista de Exercício 3 - Questão 16
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

class Fibonacci:
    def __init__(self):
        self.serie = []

    def gerar_serie(self):
        a, b = 0, 1
        while a <= 500:
            self.serie.append(a)
            a, b = b, a + b

    def exibir_serie(self):
        print("Série de Fibonacci até o valor 500:")
        for numero in self.serie:
            print(numero)


def main():
    fibonacci = Fibonacci()
    fibonacci.gerar_serie()
    fibonacci.exibir_serie()


if __name__ == "__main__":
    main()
