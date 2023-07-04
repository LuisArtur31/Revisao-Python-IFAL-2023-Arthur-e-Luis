#Lista de Exercício 3 - Questão 21
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

class Primo:
    def is_primo(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


def main():
    primo = Primo()

    try:
        num = int(input("Digite um número inteiro: "))
        if primo.is_primo(num):
            print(f"{num} é um número primo.")
        else:
            print(f"{num} não é um número primo.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")


if __name__ == "__main__":
    main()
