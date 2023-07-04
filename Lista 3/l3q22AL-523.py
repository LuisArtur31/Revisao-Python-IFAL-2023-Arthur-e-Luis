#Lista de Exercício 3 - Questão 22
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

class Primo:
    def is_primo(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def divisores(self, num):
        divisores = []
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisores.append(i)
                if i != num // i:
                    divisores.append(num // i)
        return sorted(divisores)


def main():
    primo = Primo()

    try:
        num = int(input("Digite um número inteiro: "))
        if primo.is_primo(num):
            print(f"{num} é um número primo.")
        else:
            print(f"{num} não é um número primo.")
            print(f"Divisores de {num}: {primo.divisores(num)}")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")


if __name__ == "__main__":
    main()
