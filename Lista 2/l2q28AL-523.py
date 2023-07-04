#Lista de Exercício 2 - Questão 28
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

class HipermercadoTabajara:
    def __init__(self):
        self.promocoes = {
            "File Duplo": {"ate_5kg": 4.90, "acima_5kg": 5.80},
            "Alcatra": {"ate_5kg": 5.90, "acima_5kg": 6.80},
            "Picanha": {"ate_5kg": 6.90, "acima_5kg": 7.80}
        }
        self.desconto_cartao_tabajara = 0.05

    def calcular_valor_total(self, tipo_carne, quantidade_kg, usar_cartao_tabajara):
        if tipo_carne not in self.promocoes:
            raise ValueError("Tipo de carne inválido.")

        if quantidade_kg <= 5:
            preco_kg = self.promocoes[tipo_carne]["ate_5kg"]
        else:
            preco_kg = self.promocoes[tipo_carne]["acima_5kg"]

        valor_total = preco_kg * quantidade_kg

        if usar_cartao_tabajara:
            desconto = valor_total * self.desconto_cartao_tabajara
            valor_total -= desconto

        return valor_total


def main():
    hipermercado = HipermercadoTabajara()

    try:
        tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra ou Picanha): ")
        quantidade_kg = float(input("Digite a quantidade em kg: "))
        usar_cartao_tabajara = input("Deseja utilizar o cartão Tabajara? (S-sim ou N-não): ").upper() == "S"

        valor_total = hipermercado.calcular_valor_total(tipo_carne, quantidade_kg, usar_cartao_tabajara)
        desconto = valor_total * hipermercado.desconto_cartao_tabajara if usar_cartao_tabajara else 0
        valor_a_pagar = valor_total - desconto

        print("CUPOM FISCAL")
        print("Tipo de carne:", tipo_carne)
        print("Quantidade (kg):", quantidade_kg)
        print("Preço total: R$", valor_total)
        print("Tipo de pagamento: Cartão Tabajara" if usar_cartao_tabajara else "Tipo de pagamento: Outro")
        print("Desconto: R$", desconto)
        print("Valor a pagar: R$", valor_a_pagar)
    except ValueError as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
