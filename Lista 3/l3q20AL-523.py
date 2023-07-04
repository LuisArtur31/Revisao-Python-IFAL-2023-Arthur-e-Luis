#Lista de Exercício 3 - Questão 20
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

class Fatorial:
    def calcular_fatorial(self, n):
        if n < 0 or n > 15:
            raise ValueError("O número deve ser um inteiro positivo menor que 16.")
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
            n = int(input("Digite um número inteiro positivo menor que 16 (digite 0 para sair): "))
            if n == 0:
                break
            resultado = fatorial.calcular_fatorial(n)
            print(f"O fatorial de {n} é: {resultado}")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
