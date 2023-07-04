#Lista de Exercício 4 - Questão 1
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

class VetorInteiro:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.vetor = []

    def ler_vetor(self):
        for i in range(self.tamanho):
            while True:
                try:
                    numero = int(input(f"Digite o {i+1}º número inteiro: "))
                    self.vetor.append(numero)
                    break
                except ValueError:
                    print("Valor inválido. Digite um número inteiro.")

    def mostrar_vetor(self):
        print("Números informados:")
        for numero in self.vetor:
            print(numero)


def main():
    tamanho = 5
    vetor = VetorInteiro(tamanho)
    vetor.ler_vetor()
    vetor.mostrar_vetor()


if __name__ == "__main__":
    main()
