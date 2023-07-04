#Lista de Exercício 3 - Questão 48
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
#Exemplo:
#  12376489
#  => 98467321

def inverter_numero(numero):
    if numero < 0:
        raise ValueError("O número deve ser positivo.")
    
    numero_str = str(numero)
    numero_invertido = int(numero_str[::-1])
    
    return numero_invertido


# Exemplo de uso da função
try:
    numero = int(input("Digite um número inteiro positivo: "))
    numero_invertido = inverter_numero(numero)
    print(f"Número invertido: {numero_invertido}")
except ValueError as e:
    print(f"Erro: {e}")
