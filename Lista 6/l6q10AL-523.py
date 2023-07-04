#Lista de Exercício 6 - Questão 10
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

class NumeroPorExtenso:
    def __init__(self, numero):
        self.numero = numero

    def _numero_por_extenso_ate_dezena(self, numero):
        unidades = {
            1: 'um',
            2: 'dois',
            3: 'três',
            4: 'quatro',
            5: 'cinco',
            6: 'seis',
            7: 'sete',
            8: 'oito',
            9: 'nove'
        }

        especiais = {
            10: 'dez',
            11: 'onze',
            12: 'doze',
            13: 'treze',
            14: 'quatorze',
            15: 'quinze',
            16: 'dezesseis',
            17: 'dezessete',
            18: 'dezoito',
            19: 'dezenove'
        }

        dezenas = {
            2: 'vinte',
            3: 'trinta',
            4: 'quarenta',
            5: 'cinquenta',
            6: 'sessenta',
            7: 'setenta',
            8: 'oitenta',
            9: 'noventa'
        }

        if numero in unidades:
            return unidades[numero]
        elif numero in especiais:
            return especiais[numero]
        else:
            dezena, unidade = divmod(numero, 10)
            if unidade == 0:
                return dezenas[dezena]
            else:
                return f'{dezenas[dezena]} e {unidades[unidade]}'

    def numero_por_extenso(self):
        try:
            numero = int(self.numero)

            if numero < 0 or numero > 99:
                return 'Número inválido.'

            if numero < 20:
                return self._numero_por_extenso_ate_dezena(numero)
            else:
                dezena, unidade = divmod(numero, 10)
                if unidade == 0:
                    return self._numero_por_extenso_ate_dezena(numero)
                else:
                    return f'{self._numero_por_extenso_ate_dezena(dezena * 10)} e {self._numero_por_extenso_ate_dezena(unidade)}'

        except ValueError:
            return 'Valor inválido.'


def main():
    try:
        numero = input('Digite um número até 99: ')

        por_extenso = NumeroPorExtenso(numero)
        resultado = por_extenso.numero_por_extenso()
        print(resultado)

    except Exception as e:
        print(f'Ocorreu um erro: {str(e)}')


if __name__ == '__main__':
    main()
