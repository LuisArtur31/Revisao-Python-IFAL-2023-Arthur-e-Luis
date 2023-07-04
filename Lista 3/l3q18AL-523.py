#Lista de Exercício 3 - Questão 18
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

class ConjuntoNumeros:
    def __init__(self):
        self.numbers = []

    def ler_numeros(self, n):
        for i in range(n):
            while True:
                try:
                    numero = float(input(f"Digite o {i+1}º número: "))
                    self.numbers.append(numero)
                    break
                except ValueError:
                    print("Valor inválido. Digite um número válido.")

    def encontrar_menor(self):
        if not self.numbers:
            return None
        return min(self.numbers)

    def encontrar_maior(self):
        if not self.numbers:
            return None
        return max(self.numbers)

    def calcular_soma(self):
        return sum(self.numbers)


def main():
    conjunto = ConjuntoNumeros()

    while True:
        try:
            n = int(input("Digite a quantidade de números: "))
            break
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    conjunto.ler_numeros(n)

    menor = conjunto.encontrar_menor()
    maior = conjunto.encontrar_maior()
    soma = conjunto.calcular_soma()

    if menor is not None:
        print(f"Menor valor: {menor}")
    else:
        print("Não foram fornecidos números.")

    if maior is not None:
        print(f"Maior valor: {maior}")
    else:
        print("Não foram fornecidos números.")

    print(f"Soma dos valores: {soma}")


if __name__ == "__main__":
    main()
