#Lista de Exercício 6 - Questão 3
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

#F
#U
#L
#A
#N
#O

class NomeVertical:
    def __init__(self, nome):
        self.nome = nome

    def imprimir_vertical(self):
        for letra in self.nome:
            print(letra)

def main():
    try:
        nome = input('Digite o seu nome: ')

        nome_vertical = NomeVertical(nome)
        nome_vertical.imprimir_vertical()

    except Exception as e:
        print(f'Ocorreu um erro: {str(e)}')

if __name__ == '__main__':
    main()
