#Lista de Exercício 6 - Questão 1
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

#Compara duas strings
#String 1: Brasil Hexa 2006
#String 2: Brasil! Hexa 2006!
#Tamanho de "Brasil Hexa 2006": 16 caracteres
#Tamanho de "Brasil! Hexa 2006!": 18 caracteres
#As duas strings são de tamanhos diferentes.
#As duas strings possuem conteúdo diferente.

class ComparadorStrings:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    def comparar_strings(self):
        tamanho_string1 = len(self.string1)
        tamanho_string2 = len(self.string2)

        print(f'String 1: {self.string1}')
        print(f'String 2: {self.string2}')
        print(f'Tamanho de "{self.string1}": {tamanho_string1} caracteres')
        print(f'Tamanho de "{self.string2}": {tamanho_string2} caracteres')

        if tamanho_string1 == tamanho_string2:
            print('As duas strings são do mesmo tamanho.')
        else:
            print('As duas strings são de tamanhos diferentes.')

        if self.string1 == self.string2:
            print('As duas strings possuem o mesmo conteúdo.')
        else:
            print('As duas strings possuem conteúdo diferente.')


def main():
    try:
        string1 = input('Digite a primeira string: ')
        string2 = input('Digite a segunda string: ')

        comparador = ComparadorStrings(string1, string2)
        comparador.comparar_strings()

    except Exception as e:
        print(f'Ocorreu um erro: {str(e)}')


if __name__ == '__main__':
    main()
