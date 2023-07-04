#Lista de Exercício 5 - Questão 10
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random

class Craps:
    def __init__(self):
        self.ponto = 0

    def jogar_dados(self):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        total = dado1 + dado2
        print(f"Resultado do lançamento: {dado1} + {dado2} = {total}")
        return total

    def jogar(self):
        primeira_jogada = True

        while True:
            try:
                if primeira_jogada:
                    input("Pressione Enter para lançar os dados...")
                    resultado = self.jogar_dados()

                    if resultado == 7 or resultado == 11:
                        print("Natural! Você ganhou!")
                        break
                    elif resultado == 2 or resultado == 3 or resultado == 12:
                        print("Craps! Você perdeu!")
                        break
                    else:
                        self.ponto = resultado
                        print(f"Ponto estabelecido: {self.ponto}")
                        primeira_jogada = False
                else:
                    input("Pressione Enter para lançar os dados novamente...")
                    resultado = self.jogar_dados()

                    if resultado == self.ponto:
                        print("Você ganhou!")
                        break
                    elif resultado == 7:
                        print("Você perdeu!")
                        break
            except ValueError:
                print("Erro: entrada inválida. Tente novamente.")

def main():
    jogo = Craps()
    jogo.jogar()

if __name__ == "__main__":
    main()
