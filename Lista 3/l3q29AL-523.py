#Lista de Exercício 3 - Questão 29
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
#Lojas Quase Dois - Tabela de preços
#1 - R$ 1.99
#2 - R$ 3.98
#...
#50 - R$ 99.50

class TabelaPrecos:
    def __init__(self):
        self.tabela = {}

    def montar_tabela(self, quantidade_maxima):
        for i in range(1, quantidade_maxima + 1):
            preco = 1.99 * i
            self.tabela[i] = preco

    def exibir_tabela(self):
        print("Lojas Quase Dois - Tabela de preços")
        for quantidade, preco in self.tabela.items():
            print(f"{quantidade} - R$ {preco:.2f}")


def main():
    tabela_precos = TabelaPrecos()

    while True:
        try:
            quantidade_maxima = int(input("Digite a quantidade máxima de produtos na tabela (1 a 50): "))
            if quantidade_maxima < 1 or quantidade_maxima > 50:
                raise ValueError
            break
        except ValueError:
            print("Valor inválido. Digite um número inteiro entre 1 e 50.")

    tabela_precos.montar_tabela(quantidade_maxima)
    tabela_precos.exibir_tabela()


if __name__ == "__main__":
    main()

