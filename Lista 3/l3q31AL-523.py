#Lista de Exercício 3 - Questão 31
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
#Lojas Tabajara 
#Produto 1: R$ 2.20
#Produto 2: R$ 5.80
#Produto 3: R$ 0
#Total: R$ 9.00
#Dinheiro: R$ 20.00
#Troco: R$ 11.00
#...

class CaixaRegistradora:
    def __init__(self):
        self.produtos = []
        self.total = 0.0

    def registrar_compra(self):
        while True:
            try:
                preco = float(input("Digite o preço do produto (ou 0 para finalizar a compra): "))
                if preco < 0:
                    raise ValueError
                elif preco == 0:
                    break
                self.produtos.append(preco)
                self.total += preco
            except ValueError:
                print("Valor inválido. Digite um preço válido.")

    def calcular_troco(self, dinheiro):
        troco = dinheiro - self.total
        return troco

    def reiniciar_compra(self):
        self.produtos = []
        self.total = 0.0

    def exibir_compra(self):
        print("Lojas Tabajara")
        for i, preco in enumerate(self.produtos, start=1):
            print(f"Produto {i}: R$ {preco:.2f}")
        print(f"Total: R$ {self.total:.2f}")

    def executar_caixa(self):
        while True:
            self.registrar_compra()
            self.exibir_compra()

            while True:
                try:
                    dinheiro = float(input("Digite o valor em dinheiro: "))
                    if dinheiro < self.total:
                        raise ValueError
                    break
                except ValueError:
                    print("Valor inválido. Digite um valor igual ou maior que o total da compra.")

            troco = self.calcular_troco(dinheiro)
            print(f"Troco: R$ {troco:.2f}")

            self.reiniciar_compra()

            opcao = input("Deseja registrar uma nova compra? (S/N): ")
            if opcao.upper() != "S":
                break


def main():
    caixa = CaixaRegistradora()
    caixa.executar_caixa()


if __name__ == "__main__":
    main()
