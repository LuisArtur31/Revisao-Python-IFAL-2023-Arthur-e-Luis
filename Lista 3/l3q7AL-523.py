#Lista de Exercício 3 - Questão 7
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que leia 5 números e informe o maior número.

class MaiorNumero:
    def __init__(self):
        self.numbers = []

    def ler_numeros(self):
        for i in range(5):
            while True:
                try:
                    number = float(input(f"Informe o {i+1}º número: "))
                    self.numbers.append(number)
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número válido.")

    def encontrar_maior_numero(self):
        if len(self.numbers) > 0:
            return max(self.numbers)
        else:
            return None

def main():
    maior = MaiorNumero()
    maior.ler_numeros()
    maior_numero = maior.encontrar_maior_numero()

    if maior_numero is not None:
        print(f"O maior número é: {maior_numero}")
    else:
        print("Nenhum número foi informado.")

if __name__ == "__main__":
    main()
