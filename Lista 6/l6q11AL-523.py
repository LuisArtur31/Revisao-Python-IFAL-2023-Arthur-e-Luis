#Lista de Exercício 6 - Questão 11
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

import random

class JogoDaForca:
    def __init__(self):
        self.palavras = []
        self.palavra_secreta = ''
        self.letras_corretas = []
        self.letras_erradas = []

    def carregar_palavras(self, arquivo):
        try:
            with open(arquivo, 'r') as f:
                self.palavras = f.read().splitlines()
        except FileNotFoundError:
            print(f"Arquivo '{arquivo}' não encontrado.")
        except Exception as e:
            print(f"Erro ao carregar palavras: {str(e)}")

    def escolher_palavra(self):
        self.palavra_secreta = random.choice(self.palavras).upper()

    def exibir_palavra(self):
        for letra in self.palavra_secreta:
            if letra in self.letras_corretas:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print()

    def adivinhar_letra(self, letra):
        letra = letra.upper()

        if letra in self.letras_corretas or letra in self.letras_erradas:
            print(f"A letra '{letra}' já foi escolhida.")
            return

        if letra in self.palavra_secreta:
            self.letras_corretas.append(letra)
            if self._verificar_vitoria():
                print(f"Parabéns! Você venceu! A palavra era '{self.palavra_secreta}'.")
                return
        else:
            self.letras_erradas.append(letra)
            if len(self.letras_erradas) == 6:
                print("Você foi enforcado!")
                print(f"A palavra era '{self.palavra_secreta}'.")
                return

        self._exibir_status()

    def _exibir_status(self):
        print(f"Letras corretas: {', '.join(self.letras_corretas)}")
        print(f"Letras erradas: {', '.join(self.letras_erradas)}")
        print()

    def _verificar_vitoria(self):
        for letra in self.palavra_secreta:
            if letra not in self.letras_corretas:
                return False
        return True


def main():
    jogo = JogoDaForca()
    jogo.carregar_palavras('palavras.txt')
    jogo.escolher_palavra()

    while True:
        jogo.exibir_palavra()
        letra = input("Digite uma letra: ")

        if letra == '':
            print("Por favor, digite uma letra válida.")
            continue

        jogo.adivinhar_letra(letra)

        if len(jogo.letras_erradas) == 6 or jogo._verificar_vitoria():
            break


if __name__ == '__main__':
    main()
