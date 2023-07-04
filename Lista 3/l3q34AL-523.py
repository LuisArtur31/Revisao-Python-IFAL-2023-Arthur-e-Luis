#Lista de Exercício 3 - Questão 34
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

class P:
    def vrfcr_primo(self):
        try:
            numero = int(input("Digite um número inteiro: "))
            if numero < 2:
                raise ValueError("O número deve ser maior ou igual a 2.")
        except ValueError as e:
            print(f"Entrada inválida: {e}")
            return

        if self.eh_primo(numero):
            print(f"{numero} é um número primo.")
        else:
            print(f"{numero} não é um número primo.")

    def eh_primo(self, numero):
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True


def main():
    primo = P()
    primo.vrfcr_primo()


if __name__ == "__main__":
    main()
