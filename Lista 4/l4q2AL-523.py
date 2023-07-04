#Lista de Exercício 4 - Questão 2
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

class Vetor:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.numeros = []

    def ler_numeros(self):
        for i in range(self.tamanho):
            while True:
                try:
                    numero = float(input(f"Digite o número {i+1}: "))
                    break
                except ValueError:
                    print("Valor inválido. Digite um número válido.")
            self.numeros.append(numero)

    def mostrar_inverso(self):
        print("Vetor na ordem inversa:")
        for numero in reversed(self.numeros):
            print(numero)


def main():
    vetor = Vetor(10)
    vetor.ler_numeros()
    vetor.mostrar_inverso()


# Execução do programa
if __name__ == '__main__':
    main()
