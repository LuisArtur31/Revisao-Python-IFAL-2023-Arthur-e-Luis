#Lista de Exercício 1 - Questão 16
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

class TamanhoInvalidoException(Exception):
    pass


class CalculadoraTinta:
    def __init__(self):
        self.area_pintada = None

    def ler_area_pintada(self):
        while True:
            try:
                self.area_pintada = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))
                if self.area_pintada <= 0:
                    raise TamanhoInvalidoException("Tamanho inválido. Digite um valor positivo.")
                break
            except ValueError:
                print("Valor inválido. Digite um número.")
            except TamanhoInvalidoException as e:
                print(f"Erro: {str(e)}")

    def calcular_quantidade_latas(self):
        if self.area_pintada is None:
            raise TamanhoInvalidoException("Nenhum tamanho de área foi informado.")

        cobertura_litro = 3
        capacidade_lata = 18
        preco_lata = 80

        litros_necessarios = self.area_pintada / cobertura_litro
        latas_necessarias = int(litros_necessarios / capacidade_lata)
        if litros_necessarios % capacidade_lata != 0:
            latas_necessarias += 1
        preco_total = latas_necessarias * preco_lata

        return latas_necessarias, preco_total


def main():
    calculadora = CalculadoraTinta()

    try:
        calculadora.ler_area_pintada()
        latas_necessarias, preco_total = calculadora.calcular_quantidade_latas()
        print(f"Quantidade de latas de tinta necessárias: {latas_necessarias}")
        print(f"Preço total: R$ {preco_total:.2f}")
    except TamanhoInvalidoException as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
