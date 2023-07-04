#Lista de Exercício 2 - Questão 21
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

class CaixaEletronico:
    def __init__(self):
        self.notas_disponiveis = [100, 50, 10, 5, 1]

    def efetuar_saque(self, valor_saque):
        if valor_saque < 10 or valor_saque > 600:
            raise ValueError("O valor de saque deve ser entre 10 e 600 reais.")

        resultado = {}

        for nota in self.notas_disponiveis:
            quantidade = valor_saque // nota
            if quantidade > 0:
                resultado[nota] = quantidade
                valor_saque -= quantidade * nota

        return resultado


try:
    caixa = CaixaEletronico()

    valor_saque = int(input("Digite o valor de saque (entre 10 e 600 reais): "))

    notas_entregues = caixa.efetuar_saque(valor_saque)

    print("Notas fornecidas:")
    for nota, quantidade in notas_entregues.items():
        if quantidade > 0:
            if quantidade == 1:
                print(f"{quantidade} nota de {nota} reais")
            else:
                print(f"{quantidade} notas de {nota} reais")
except ValueError as error:
    print(error)
