#Lista de Exercício 2 - Questão 26
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

class PostoCombustivel:
    def __init__(self):
        self.preco_gasolina = 2.50
        self.preco_alcool = 1.90

    def calcular_valor_pago(self, tipo_combustivel, quantidade_litros):
        if tipo_combustivel == 'G':
            preco_litro = self.preco_gasolina
            if quantidade_litros <= 20:
                desconto_por_litro = 0.04
            else:
                desconto_por_litro = 0.06
        elif tipo_combustivel == 'A':
            preco_litro = self.preco_alcool
            if quantidade_litros <= 20:
                desconto_por_litro = 0.03
            else:
                desconto_por_litro = 0.05
        else:
            raise ValueError("Tipo de combustível inválido. Digite 'A' para álcool ou 'G' para gasolina.")

        valor_total = preco_litro * quantidade_litros
        desconto_total = desconto_por_litro * quantidade_litros * preco_litro
        valor_pago = valor_total - desconto_total

        return valor_pago


def main():
    posto = PostoCombustivel()

    try:
        tipo_combustivel = input("Digite o tipo de combustível (A-álcool ou G-gasolina): ")
        quantidade_litros = float(input("Digite a quantidade de litros vendidos: "))

        valor_pago = posto.calcular_valor_pago(tipo_combustivel.upper(), quantidade_litros)

        print(f"Valor a ser pago: R$ {valor_pago:.2f}")
    except ValueError as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
