#Lista de Exercício 6 - Questão 5
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

#FULANO
#FULAN
#FULA
#FUL
#FU
#F

class NomeEscadaInvertida:
    def __init__(self, nome):
        self.nome = nome

    def imprimir_escada_invertida(self):
        for i in range(len(self.nome), 0, -1):
            print(self.nome[:i])

def main():
    try:
        nome = input('Digite o seu nome: ')

        nome_escada_invertida = NomeEscadaInvertida(nome)
        nome_escada_invertida.imprimir_escada_invertida()

    except Exception as e:
        print(f'Ocorreu um erro: {str(e)}')

if __name__ == '__main__':
    main()
