#Lista de Exercício 6 - Questão 8
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

class VerificadorPalindromo:
    def __init__(self, frase):
        self.frase = self._formatar_frase(frase)

    def _formatar_frase(self, frase):
        # Remove espaços em branco e pontuações da frase
        frase_formatada = ''.join(c.lower() for c in frase if c.isalnum())
        return frase_formatada

    def verificar_palindromo(self):
        # Verifica se a frase é um palíndromo
        return self.frase == self.frase[::-1]

    def executar_verificacao(self):
        try:
            print(f'Frase: {self.frase}')
            if self.verificar_palindromo():
                print('É um palíndromo.')
            else:
                print('Não é um palíndromo.')

        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')


def main():
    try:
        frase = input('Digite uma frase: ')

        verificador = VerificadorPalindromo(frase)
        verificador.executar_verificacao()

    except Exception as e:
        print(f'Ocorreu um erro: {str(e)}')


if __name__ == '__main__':
    main()
