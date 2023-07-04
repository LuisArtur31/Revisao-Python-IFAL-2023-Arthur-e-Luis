#Lista de Exercício 3 - Questão 8
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que leia 5 números e informe a soma e a média dos números.

class Calculadora:
    def __init__(self):
        self.numbers = []

    def ler_numeros(self):
        for i in range(5):
            while True:
                try:
                    num = float(input(f"Digite o {i+1}º número: "))
                    self.numbers.append(num)
                    break
                except ValueError:
                    print("Valor inválido. Digite um número válido.")

    def calcular_soma(self):
        return sum(self.numbers)

    def calcular_media(self):
        return sum(self.numbers) / len(self.numbers)


def main():
    calculadora = Calculadora()
    calculadora.ler_numeros()

    soma = calculadora.calcular_soma()
    media = calculadora.calcular_media()

    print(f"Soma dos números: {soma}")
    print(f"Média dos números: {media}")


if __name__ == "__main__":
    main()
