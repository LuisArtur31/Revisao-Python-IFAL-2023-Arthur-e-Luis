#Lista de Exercício 2 - Questão 14
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

class ValorInvalidoException(Exception):
    pass


class Aluno:
    def __init__(self):
        self.nota1 = 0.0
        self.nota2 = 0.0

    def ler_notas(self):
        try:
            self.nota1 = float(input("Digite a primeira nota: "))
            self.nota2 = float(input("Digite a segunda nota: "))

            if self.nota1 < 0 or self.nota1 > 10 or self.nota2 < 0 or self.nota2 > 10:
                raise ValorInvalidoException("Valor inválido. As notas devem estar entre 0.0 e 10.0.")
        except ValueError:
            raise ValorInvalidoException("Valor inválido. Digite um número válido.")

    def calcular_media(self):
        media = (self.nota1 + self.nota2) / 2
        return media

    def obter_conceito(self, media):
        if media >= 9.0:
            conceito = "A"
        elif media >= 7.5:
            conceito = "B"
        elif media >= 6.0:
            conceito = "C"
        elif media >= 4.0:
            conceito = "D"
        else:
            conceito = "E"
        return conceito

    def imprimir_resultado(self, media, conceito):
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}")
        print(f"Média: {media}")
        print(f"Conceito: {conceito}")

        if conceito in ["A", "B", "C"]:
            print("APROVADO")
        else:
            print("REPROVADO")


def main():
    try:
        aluno = Aluno()
        aluno.ler_notas()
        media = aluno.calcular_media()
        conceito = aluno.obter_conceito(media)
        aluno.imprimir_resultado(media, conceito)
    except ValorInvalidoException as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
