#Lista de Exercício 2 - Questão 13
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

class DiaSemana:
    def __init__(self, numero):
        self.numero = numero

    def obter_dia_semana(self):
        if self.numero == 1:
            return "Domingo"
        elif self.numero == 2:
            return "Segunda-feira"
        elif self.numero == 3:
            return "Terça-feira"
        elif self.numero == 4:
            return "Quarta-feira"
        elif self.numero == 5:
            return "Quinta-feira"
        elif self.numero == 6:
            return "Sexta-feira"
        elif self.numero == 7:
            return "Sábado"
        else:
            raise ValueError("Valor inválido. Digite um número de 1 a 7.")

try:
    numero = int(input("Digite um número de 1 a 7: "))
    dia = DiaSemana(numero)
    dia_da_semana = dia.obter_dia_semana()
    print(f"O dia correspondente ao número {numero} é {dia_da_semana}.")
except ValueError as error:
    print(error)

