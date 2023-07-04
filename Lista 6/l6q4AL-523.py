#Lista de Exercício 6 - Questão 4
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

#F
#FU
#FUL
#FULA
#FULAN
#FULANO

class NomeEscada:
    def __init__(self, nome):
        self.nome = nome

    def imprimir_escada(self):
        for i in range(1, len(self.nome) + 1):
            print(self.nome[:i])

def main():
    try:
        nome = input('Digite o seu nome: ')

        nome_escada = NomeEscada(nome)
        nome_escada.imprimir_escada()

    except Exception as e:
        print(f'Ocorreu um erro: {str(e)}')

if __name__ == '__main__':
    main()
