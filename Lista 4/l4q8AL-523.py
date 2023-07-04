#Lista de Exercício 4 - Questão 8
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

class Pessoa:
    def __init__(self, idade, altura):
        self.idade = idade
        self.altura = altura


def main():
    idades = []
    alturas = []

    for i in range(5):
        while True:
            try:
                idade = int(input(f"Digite a idade da pessoa {i+1}: "))
                altura = float(input(f"Digite a altura da pessoa {i+1}: "))
                break
            except ValueError:
                print("Valor inválido. Digite um número válido.")

        idades.append(idade)
        alturas.append(altura)

    print("Idades (em ordem inversa):")
    for idade in reversed(idades):
        print(idade)

    print("\nAlturas (em ordem inversa):")
    for altura in reversed(alturas):
        print(altura)


# Execução do programa
if __name__ == '__main__':
    main()
