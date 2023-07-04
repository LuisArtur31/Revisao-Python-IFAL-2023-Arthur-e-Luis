#Lista de Exercício 3 - Questão 30
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
#preço do pão: R$ 0.18
#Panificadora Pão de Ontem - Tabela de preços
#1 - R$ 0.18
#2 - R$ 0.36
#...
#50 - R$ 9.00

class TabelaPrecosPao:
    def __init__(self):
        self.preco_pao = 0

    def obter_preco_pao(self):
        try:
            self.preco_pao = float(input("Digite o preço do pão: R$ "))
            if self.preco_pao <= 0:
                raise ValueError("O preço do pão deve ser um valor positivo.")
        except ValueError as e:
            print(f"Entrada inválida: {e}")
            return

        self.exibir_tabela_precos()

    def exibir_tabela_precos(self):
        print("Panificadora Pão de Ontem - Tabela de preços")
        for quantidade_paos in range(1, 51):
            valor_total = self.preco_pao * quantidade_paos
            print(f"{quantidade_paos} - R$ {valor_total:.2f}")


def main():
    tabela_precos_pao = TabelaPrecosPao()
    tabela_precos_pao.obter_preco_pao()


if __name__ == "__main__":
    main()
