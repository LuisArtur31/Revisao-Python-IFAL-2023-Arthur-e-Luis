#Lista de Exercício 4 - Questão 6
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def ler_notas(self):
        for i in range(4):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i+1} do aluno {self.nome}: "))
                    if nota < 0 or nota > 10:
                        raise ValueError
                    break
                except ValueError:
                    print("Valor inválido. Digite um número entre 0 e 10.")
            self.notas.append(nota)

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)


def main():
    alunos = []
    for i in range(10):
        nome = input(f"Digite o nome do aluno {i+1}: ")
        aluno = Aluno(nome)
        aluno.ler_notas()
        alunos.append(aluno)

    qtd_alunos_aprovados = 0
    for aluno in alunos:
        media = aluno.calcular_media()
        if media >= 7.0:
            qtd_alunos_aprovados += 1

    print(f"Número de alunos com média maior ou igual a 7.0: {qtd_alunos_aprovados}")


# Execução do programa
if __name__ == '__main__':
    main()
