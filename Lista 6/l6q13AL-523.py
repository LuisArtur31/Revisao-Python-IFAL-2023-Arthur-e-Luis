#Lista de Exercício 6 - Questão 13
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

import random

class JogoAdivinhacao:
    def __init__(self):
        self.palavras = self.carregar_palavras()
        self.palavra_secreta = self.escolher_palavra()
        self.palavra_embaralhada = self.embaralhar_palavra(self.palavra_secreta)
        self.tentativas = 6

    def carregar_palavras(self):
        try:
            with open('palavras.txt', 'r') as arquivo:
                palavras = [palavra.strip().lower() for palavra in arquivo.readlines()]
                return palavras
        except Exception as e:
            print(f'Ocorreu um erro ao carregar as palavras: {str(e)}')
            return []

    def escolher_palavra(self):
        return random.choice(self.palavras)

    def embaralhar_palavra(self, palavra):
        letras = list(palavra)
        random.shuffle(letras)
        return ''.join(letras)

    def jogar(self):
        print("Bem-vindo ao jogo de adivinhar palavras!")
        print("Adivinhe a palavra embaralhada. Você tem 6 tentativas.")
        print(f"Palavra embaralhada: {self.palavra_embaralhada}")

        while self.tentativas > 0:
            tentativa = input("Digite sua tentativa: ").lower()

            if tentativa == self.palavra_secreta:
                print("Parabéns! Você acertou a palavra!")
                return

            print("Você errou!")

            self.tentativas -= 1
            if self.tentativas > 0:
                print(f"Tentativas restantes: {self.tentativas}")
            else:
                print(f"Suas tentativas acabaram. A palavra correta era: {self.palavra_secreta}")

        print("Fim do jogo. Obrigado por jogar!")

def main():
    jogo = JogoAdivinhacao()
    jogo.jogar()

if __name__ == '__main__':
    main()
