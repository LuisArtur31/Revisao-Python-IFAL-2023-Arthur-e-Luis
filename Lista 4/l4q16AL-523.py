#Lista de Exercício 4 - Questão 16
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
#$200 - $299
#$300 - $399
#$400 - $499
#$500 - $599
#$600 - $699
#$700 - $799
#$800 - $899
#$900 - $999
#$1000 em diante
#Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

def calcular_salario(vendas_brutas):
    salario_base = 200
    comissao = vendas_brutas * 0.09
    salario_total = salario_base + comissao
    return salario_total

def classificar_salarios(vendedores):
    faixas_salarios = [0] * 9
    for vendas_brutas in vendedores:
        salario = calcular_salario(vendas_brutas)
        indice = min(int((salario - 200) / 100), 8)
        faixas_salarios[indice] += 1
    return faixas_salarios

def main():
    vendedores = []
    while True:
        vendas_brutas = input("Digite o valor das vendas brutas (ou 'sair' para encerrar): ")
        if vendas_brutas.lower() == "sair":
            break
        try:
            vendas_brutas = float(vendas_brutas)
            vendedores.append(vendas_brutas)
        except ValueError:
            print("Valor inválido. Digite um número válido ou 'sair' para encerrar.")

    resultados = classificar_salarios(vendedores)
    faixas = ["$200 - $299", "$300 - $399", "$400 - $499", "$500 - $599",
              "$600 - $699", "$700 - $799", "$800 - $899", "$900 - $999", "$1000 em diante"]
    
    print("Quantidade de vendedores por faixa salarial:")
    for i in range(len(faixas)):
        print(faixas[i] + ": " + str(resultados[i]))

if __name__ == "__main__":
    main()
