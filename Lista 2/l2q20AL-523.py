#Lista de Exercício 2 - Questão 20
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

class NotaInvalidaException(Exception):
    pass


class Aluno:
    def __init__(self, nota1, nota2, nota3):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_media(self):
        if any(nota < 0 or nota > 10 for nota in [self.nota1, self.nota2, self.nota3]):
            raise NotaInvalidaException("Uma ou mais notas são inválidas.")

        media = (self.nota1 + self.nota2 + self.nota3) / 3
        return media

    def verificar_aprovacao(self):
        media = self.calcular_media()

        if media == 10:
            return "Aprovado com Distinção", media
        elif media >= 7:
            return "Aprovado", media
        else:
            return "Reprovado", media


def main():
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))

        aluno = Aluno(nota1, nota2, nota3)
        resultado, media = aluno.verificar_aprovacao()
        print(f"Resultado: {resultado}")
        print(f"Média: {media:.2f}")
    except (ValueError, NotaInvalidaException) as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
