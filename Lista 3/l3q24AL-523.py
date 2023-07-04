#Lista de Exercício 3 - Questão 24
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que calcule o mostre a média aritmética de N notas.

class MediaAritmetica:
    def calcular_media(self, notas):
        quantidade = len(notas)
        if quantidade == 0:
            return 0
        soma = sum(notas)
        return soma / quantidade


def main():
    media = MediaAritmetica()

    try:
        n = int(input("Quantidade de notas: "))
        notas = []
        for i in range(n):
            nota = float(input(f"Nota {i+1}: "))
            notas.append(nota)
        media_final = media.calcular_media(notas)
        print(f"Média: {media_final}")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro para a quantidade de notas e um número real para cada nota.")


if __name__ == "__main__":
    main()
