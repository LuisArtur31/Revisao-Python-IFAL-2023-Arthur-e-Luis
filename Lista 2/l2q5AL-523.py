#Lista de Exercício 2 - Questão 5
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

class CalculadoraMedia:
    def __init__(self):
        self.nota1 = None
        self.nota2 = None

    def solicitar_notas(self):
        while True:
            try:
                self.nota1 = float(input("Digite a primeira nota: "))
                self.nota2 = float(input("Digite a segunda nota: "))
                break
            except ValueError:
                print("Digite apenas valores numéricos!")

    def calcular_media(self):
        media = (self.nota1 + self.nota2) / 2
        return media


try:
    calculadora = CalculadoraMedia()
    calculadora.solicitar_notas()
    media_alcancada = calculadora.calcular_media()

    if media_alcancada == 10:
        print("Aprovado com Distinção")
    elif media_alcancada >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
