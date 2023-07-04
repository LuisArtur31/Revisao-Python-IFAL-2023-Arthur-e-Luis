#Lista de Exercício 2 - Questão 17
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

class AnoBissexto:
    def __init__(self, ano):
        self.ano = ano

    def verificar_bissexto(self):
        if self.ano % 4 == 0 and (self.ano % 100 != 0 or self.ano % 400 == 0):
            return True
        else:
            return False


try:
    ano = int(input("Digite um ano: "))

    ano_bissexto = AnoBissexto(ano)

    if ano_bissexto.verificar_bissexto():
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número de ano válido.")
