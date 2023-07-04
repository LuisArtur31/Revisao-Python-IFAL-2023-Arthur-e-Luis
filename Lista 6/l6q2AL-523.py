#Lista de Exercício 6 - Questão 2
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

class NomeReverso:
    def __init__(self, nome):
        self.nome = nome

    def inverter_nome(self):
        nome_invertido = self.nome.upper()[::-1]
        return nome_invertido

def main():
    try:
        nome = input('Digite o seu nome: ')

        nome_reverso = NomeReverso(nome)
        nome_invertido = nome_reverso.inverter_nome()

        print(f'Nome invertido: {nome_invertido}')

    except Exception as e:
        print(f'Ocorreu um erro: {str(e)}')

if __name__ == '__main__':
    main()
