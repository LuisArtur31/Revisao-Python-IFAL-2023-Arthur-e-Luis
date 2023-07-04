#Lista de Exercício 5 - Questão 5
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

class Item:
    def __init__(self, custo):
        self.custo = custo

    def somaImposto(self, taxaImposto):
        imposto = self.custo * (taxaImposto / 100)
        custoTotal = self.custo + imposto
        return custoTotal

def main():
    try:
        taxa = float(input("Digite a taxa de imposto sobre vendas em porcentagem: "))
        custoItem = float(input("Digite o custo do item antes do imposto: "))

        item = Item(custoItem)
        custoFinal = item.somaImposto(taxa)

        print("O custo do item com imposto é:", custoFinal)

    except ValueError:
        print("Erro: Valor inválido. Certifique-se de digitar números corretos.")

if __name__ == "__main__":
    main()

