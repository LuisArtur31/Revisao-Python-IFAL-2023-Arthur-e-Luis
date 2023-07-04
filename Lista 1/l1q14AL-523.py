#Lista de Exercício 1 - Questão 14
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

class PesoInvalidoException(Exception):
    pass


class CalculadoraMulta:
    def __init__(self):
        self.peso_peixes = None

    def ler_peso_peixes(self):
        while True:
            try:
                self.peso_peixes = float(input("Digite o peso dos peixes (em quilos): "))
                if self.peso_peixes <= 0:
                    raise PesoInvalidoException("Peso inválido. Digite um valor positivo.")
                break
            except ValueError:
                print("Valor inválido. Digite um número.")
            except PesoInvalidoException as e:
                print(f"Erro: {str(e)}")

    def calcular_excesso_multa(self):
        if self.peso_peixes is None:
            raise PesoInvalidoException("Nenhum peso de peixes foi informado.")

        limite_peso = 50
        excesso = max(self.peso_peixes - limite_peso, 0)
        multa = excesso * 4
        return excesso, multa


def main():
    calculadora = CalculadoraMulta()

    try:
        calculadora.ler_peso_peixes()
        excesso, multa = calculadora.calcular_excesso_multa()
        if excesso == 0:
            print("Não há excesso de peso. Nenhuma multa será aplicada.")
        else:
            print(f"Excesso de peso: {excesso:.2f} kg")
            print(f"Multa a ser paga: R$ {multa:.2f}")
    except PesoInvalidoException as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
