#Lista de Exercício 3 - Questão 43
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#O cardápio de uma lanchonete é o seguinte:
#Especificação   Código  Preço
#Cachorro Quente 100     R$ 1,20
#Bauru Simples   101     R$ 1,30
#Bauru com ovo   102     R$ 1,50
#Hambúrguer      103     R$ 1,20
#Cheeseburguer   104     R$ 1,30
#Refrigerante    105     R$ 1,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

class Lanchonete:
    def __init__(self):
        self.cardapio = {
            100: ("Cachorro Quente", 1.20),
            101: ("Bauru Simples", 1.30),
            102: ("Bauru com ovo", 1.50),
            103: ("Hambúrguer", 1.20),
            104: ("Cheeseburguer", 1.30),
            105: ("Refrigerante", 1.00)
        }
        self.pedido = {}

    def fazer_pedido(self):
        while True:
            try:
                codigo = int(input("Digite o código do item (ou 0 para encerrar o pedido): "))
                if codigo == 0:
                    break
                quantidade = int(input("Digite a quantidade desejada: "))

                if codigo in self.cardapio:
                    item = self.cardapio[codigo]
                    nome = item[0]
                    preco = item[1]
                    valor_item = preco * quantidade
                    self.pedido[nome] = valor_item
                else:
                    print("Código inválido. Digite um código válido.")

            except ValueError:
                print("Entrada inválida. Digite um número inteiro válido.")

    def calcular_total(self):
        total = sum(self.pedido.values())
        return total

    def exibir_pedido(self):
        print("\n----- Pedido -----\n")
        for nome, valor_item in self.pedido.items():
            print(f"{nome}: R$ {valor_item:.2f}")

        total = self.calcular_total()
        print(f"\nTotal do pedido: R$ {total:.2f}")


def main():
    lanchonete = Lanchonete()
    lanchonete.fazer_pedido()
    lanchonete.exibir_pedido()


if __name__ == "__main__":
    main()
