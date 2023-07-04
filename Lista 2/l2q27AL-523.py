#Lista de Exercício 2 - Questão 27
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

class Fruteira:
    def __init__(self):
        self.preco_morango_ate_5kg = 2.50
        self.preco_morango_acima_5kg = 2.20
        self.preco_maca_ate_5kg = 1.80
        self.preco_maca_acima_5kg = 1.50
        self.limite_desconto_kg = 8
        self.limite_desconto_valor = 25.00
        self.desconto = 0.10

    def calcular_valor_pago(self, kg_morangos, kg_macas):
        if kg_morangos <= 0 or kg_macas <= 0:
            raise ValueError("A quantidade de morangos e maçãs deve ser maior que zero.")

        valor_total_morangos = self.calcular_valor_fruta(kg_morangos, self.preco_morango_ate_5kg, self.preco_morango_acima_5kg)
        valor_total_macas = self.calcular_valor_fruta(kg_macas, self.preco_maca_ate_5kg, self.preco_maca_acima_5kg)

        valor_total = valor_total_morangos + valor_total_macas

        if kg_morangos + kg_macas > self.limite_desconto_kg or valor_total > self.limite_desconto_valor:
            valor_desconto = valor_total * self.desconto
            valor_total -= valor_desconto

        return valor_total

    def calcular_valor_fruta(self, kg, preco_ate_5kg, preco_acima_5kg):
        if kg <= 5:
            return kg * preco_ate_5kg
        else:
            return kg * preco_acima_5kg


try:
    fruteira = Fruteira()

    kg_morangos = float(input("Digite a quantidade de morangos (em Kg): "))
    kg_macas = float(input("Digite a quantidade de maçãs (em Kg): "))

    valor_pago = fruteira.calcular_valor_pago(kg_morangos, kg_macas)

    print(f"Valor a ser pago: R${valor_pago:.2f}")
except ValueError as error:
    print(error)
except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
