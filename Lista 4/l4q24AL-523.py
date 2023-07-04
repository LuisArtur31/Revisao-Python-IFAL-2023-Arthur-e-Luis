#Lista de Exercício 4 - Questão 
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

import random


class LancamentoDados:
    def __init__(self):
        self.resultados = []

    def lancar_dados(self, num_lancamentos):
        for _ in range(num_lancamentos):
            resultado = random.randint(1, 6)
            self.resultados.append(resultado)

    def contar_resultados(self):
        contadores = [0] * 6

        for resultado in self.resultados:
            contadores[resultado - 1] += 1

        return contadores


def main():
    try:
        num_lancamentos = int(input("Digite o número de lançamentos de dados: "))

        if num_lancamentos <= 0:
            print("Número inválido. Digite um valor maior que zero.")
            return

        lancamento = LancamentoDados()
        lancamento.lancar_dados(num_lancamentos)
        resultados = lancamento.contar_resultados()

        print("\nResultados:")
        for i, resultado in enumerate(resultados):
            print(f"Valor {i+1}: {resultado} vezes")

    except ValueError:
        print("Valor inválido. Digite um número inteiro.")


if __name__ == "__main__":
    main()
