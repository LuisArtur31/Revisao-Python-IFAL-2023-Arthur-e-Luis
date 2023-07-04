#Lista de Exercício 3 - Questão 35
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

class NumerosPrimos:
    def __init__(self):
        self.primos = []

    def verificar_primo(self, num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def gerar_primos(self, limite):
        for num in range(2, limite + 1):
            if self.verificar_primo(num):
                self.primos.append(num)

    def exibir_primos(self):
        if not self.primos:
            print("Nenhum número primo encontrado.")
        else:
            print("Números primos encontrados:")
            for num in self.primos:
                print(num)


def main():
    numeros_primos = NumerosPrimos()

    while True:
        try:
            limite = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("Valor inválido. Digite um número inteiro válido.")

    numeros_primos.gerar_primos(limite)
    numeros_primos.exibir_primos()


if __name__ == "__main__":
    main()
