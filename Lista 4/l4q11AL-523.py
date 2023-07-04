#Lista de Exercício 4 - Questão 11
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

class VetorIntercalado:
    def __init__(self):
        self.vetor1 = []
        self.vetor2 = []
        self.vetor3 = []
        self.vetor_intercalado = []

    def ler_vetores(self):
        print("Digite os elementos do primeiro vetor:")
        for i in range(10):
            while True:
                try:
                    elemento = int(input(f"Digite o elemento {i+1}: "))
                    self.vetor1.append(elemento)
                    break
                except ValueError:
                    print("Valor inválido. Digite um número inteiro.")

        print("Digite os elementos do segundo vetor:")
        for i in range(10):
            while True:
                try:
                    elemento = int(input(f"Digite o elemento {i+1}: "))
                    self.vetor2.append(elemento)
                    break
                except ValueError:
                    print("Valor inválido. Digite um número inteiro.")

        print("Digite os elementos do terceiro vetor:")
        for i in range(10):
            while True:
                try:
                    elemento = int(input(f"Digite o elemento {i+1}: "))
                    self.vetor3.append(elemento)
                    break
                except ValueError:
                    print("Valor inválido. Digite um número inteiro.")

    def intercalar_vetores(self):
        for i in range(10):
            self.vetor_intercalado.append(self.vetor1[i])
            self.vetor_intercalado.append(self.vetor2[i])
            self.vetor_intercalado.append(self.vetor3[i])

    def mostrar_vetores(self):
        print("Primeiro vetor:", self.vetor1)
        print("Segundo vetor:", self.vetor2)
        print("Terceiro vetor:", self.vetor3)
        print("Vetor intercalado:", self.vetor_intercalado)


def main():
    vetor_intercalado = VetorIntercalado()
    vetor_intercalado.ler_vetores()
    vetor_intercalado.intercalar_vetores()
    vetor_intercalado.mostrar_vetores()


if __name__ == "__main__":
    main()

