#Lista de Exercício 3 - Questão 23
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

class Primos:
    def __init__(self):
        self.divisoes = 0

    def eh_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            self.divisoes += 1
            if n % i == 0:
                return False
        return True

    def encontrar_primos(self, n):
        primos = []
        for i in range(1, n + 1):
            if self.eh_primo(i):
                primos.append(i)
        return primos


def main():
    primos = Primos()

    while True:
        try:
            n = int(input("Digite um número inteiro: "))
            if n < 1:
                raise ValueError
            break
        except ValueError:
            print("Valor inválido. Digite um número inteiro positivo.")

    numeros_primos = primos.encontrar_primos(n)
    num_divisoes = primos.divisoes

    print("Números primos:")
    for primo in numeros_primos:
        print(primo)

    print(f"Número de divisões: {num_divisoes}")


if __name__ == "__main__":
    main()
