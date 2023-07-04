#Lista de Exercício 4 - Questão 3
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

class Notas:
    def __init__(self):
        self.notas = []

    def ler_notas(self):
        for i in range(4):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i+1}: "))
                    self.notas.append(nota)
                    break
                except ValueError:
                    print("Valor inválido. Digite um número.")

    def calcular_media(self):
        soma = sum(self.notas)
        media = soma / len(self.notas)
        return media

    def mostrar_notas(self):
        print("Notas informadas:")
        for i, nota in enumerate(self.notas):
            print(f"Nota {i+1}: {nota}")

    def mostrar_media(self):
        media = self.calcular_media()
        print(f"Média: {media}")


def main():
    notas = Notas()
    notas.ler_notas()
    notas.mostrar_notas()
    notas.mostrar_media()


if __name__ == "__main__":
    main()
