#Lista de Exercício 6 - Questão 7
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
#quantos espaços em branco existem na frase.
#quantas vezes aparecem as vogais a, e, i, o, u.

class ContadorEspacosEVogais:
    def __init__(self, frase):
        self.frase = frase.lower()

    def cntr_espacos(self):
        espacos = 0
        for caractere in self.frase:
            if caractere == ' ':
                espacos += 1
        return espacos

    def cntr_vogais(self):
        vogais = {'a', 'e', 'i', 'o', 'u'}
        contador = 0
        for caractere in self.frase:
            if caractere in vogais:
                contador += 1
        return contador

    def executar_contagem(self):
        try:
            espacos = self.cntr_espacos()
            vogais = self.cntr_vogais()

            print(f'Quantidade de espaços em branco: {espacos}')
            print(f'Quantidade de vogais: {vogais}')

        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')


def main():
    try:
        frase = input('Digite uma frase: ')

        contador = ContadorEspacosEVogais(frase)
        contador.executar_contagem()

    except Exception as e:
        print(f'Ocorreu um erro: {str(e)}')


if __name__ == '__main__':
    main()
