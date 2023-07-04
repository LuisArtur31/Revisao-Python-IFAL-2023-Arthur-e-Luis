#Lista de Exercício 3 - Questão 13
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

def calcular_potencia(base, expoente):
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado


def main():
    while True:
        try:
            base = int(input("Digite o número base: "))
            expoente = int(input("Digite o número expoente: "))
            break
        except ValueError:
            print("Valor inválido. Digite um número inteiro válido.")

    potencia = calcular_potencia(base, expoente)
    print(f"{base} elevado a {expoente} é igual a: {potencia}")


if __name__ == "__main__":
    main()
