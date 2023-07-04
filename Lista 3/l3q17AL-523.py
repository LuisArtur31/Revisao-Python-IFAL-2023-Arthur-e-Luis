#Lista de Exercício 3 - Questão 17
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

class Fatorial:
    def calcular_fatorial(self, n):
        if n < 0:
            raise ValueError("O número deve ser não negativo.")
        if n == 0:
            return 1
        fatorial = 1
        for i in range(1, n+1):
            fatorial *= i
        return fatorial


def main():
    fatorial = Fatorial()

    while True:
        try:
            n = int(input("Digite um número inteiro não negativo: "))
            break
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    try:
        resultado = fatorial.calcular_fatorial(n)
        print(f"O fatorial de {n} é: {resultado}")
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
