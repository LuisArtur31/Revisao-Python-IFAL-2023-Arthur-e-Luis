#Lista de Exercício 3 - Questão 39
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

class Aluno:
    def __init__(self, numero, altura):
        self.numero = numero
        self.altura = altura


class Turma:
    def __init__(self):
        self.alunos = []

    def ler_alturas(self):
        for i in range(1, 11):
            while True:
                try:
                    numero = int(input(f"Digite o número do aluno {i}: "))
                    altura = float(input(f"Digite a altura do aluno {i} (em centímetros): "))
                    aluno = Aluno(numero, altura)
                    self.alunos.append(aluno)
                    break
                except ValueError:
                    print("Valor inválido. Digite um número inteiro para o número do aluno e um número real para a altura.")

    def encontrar_aluno_mais_alto(self):
        if not self.alunos:
            return None
        mais_alto = max(self.alunos, key=lambda x: x.altura)
        return mais_alto

    def encontrar_aluno_mais_baixo(self):
        if not self.alunos:
            return None
        mais_baixo = min(self.alunos, key=lambda x: x.altura)
        return mais_baixo

    def exibir_resultados(self):
        mais_alto = self.encontrar_aluno_mais_alto()
        mais_baixo = self.encontrar_aluno_mais_baixo()

        if mais_alto:
            print("Aluno mais alto:")
            print(f"Número: {mais_alto.numero}, Altura: {mais_alto.altura:.2f}cm")
        else:
            print("Nenhum aluno cadastrado.")

        if mais_baixo:
            print("Aluno mais baixo:")
            print(f"Número: {mais_baixo.numero}, Altura: {mais_baixo.altura:.2f}cm")
        else:
            print("Nenhum aluno cadastrado.")


def main():
    turma = Turma()
    turma.ler_alturas()
    turma.exibir_resultados()


if __name__ == "__main__":
    main()
