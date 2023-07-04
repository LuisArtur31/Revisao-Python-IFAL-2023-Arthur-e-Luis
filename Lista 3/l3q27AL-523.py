#Lista de Exercício 3 - Questão 27
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

class Escola:
    def __init__(self):
        self.turmas = []

    def ler_dados_turmas(self, n):
        for i in range(n):
            while True:
                try:
                    quantidade_alunos = int(input(f"Digite a quantidade de alunos na turma {i+1}: "))
                    if quantidade_alunos < 0 or quantidade_alunos > 40:
                        raise ValueError
                    self.turmas.append(quantidade_alunos)
                    break
                except ValueError:
                    print("Valor inválido. Digite uma quantidade válida de alunos (0 a 40).")

    def calcular_media_alunos_por_turma(self):
        if not self.turmas:
            return None
        return sum(self.turmas) / len(self.turmas)


def main():
    escola = Escola()

    while True:
        try:
            quantidade_turmas = int(input("Digite a quantidade de turmas: "))
            if quantidade_turmas < 1:
                raise ValueError
            break
        except ValueError:
            print("Valor inválido. Digite um número inteiro positivo.")

    escola.ler_dados_turmas(quantidade_turmas)

    media_alunos_por_turma = escola.calcular_media_alunos_por_turma()

    if media_alunos_por_turma is not None:
        print(f"Número médio de alunos por turma: {media_alunos_por_turma:.2f}")
    else:
        print("Não há turmas na escola.")


if __name__ == "__main__":
    main()
