#Lista de Exercício 3 - Questão 50
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

def calcular_harmonica(N):
    if N <= 0:
        raise ValueError("O número de termos deve ser maior que zero.")
    
    soma = 0
    for i in range(1, N+1):
        soma += 1/i
    
    return soma


# Exemplo de uso da função
try:
    N = int(input("Digite o número de termos: "))
    resultado = calcular_harmonica(N)
    print(f"O valor de H com {N} termos é: {resultado}")
except ValueError as e:
    print(f"Erro: {e}")
