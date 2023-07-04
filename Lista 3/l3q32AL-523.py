#Lista de Exercício 3 - Questão 32
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
#Fatorial de: 5
#5! =  5 . 4 . 3 . 2 . 1 = 120

class F:
    def calcular_f(self):
        try:
            numero = int(input("Digite um número inteiro para calcular o fatorial: "))
            if numero < 0:
                raise ValueError("O número deve ser um inteiro positivo ou zero.")
        except ValueError as e:
            print(f"Entrada inválida: {e}")
            return

        fatorial = self.calcular_fatorial_iterativo(numero)
        self.exibir_resultado(numero, fatorial)

    def calcular_fatorial_iterativo(self, numero):
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

    def exibir_resultado(self, numero, fatorial):
        print(f"Fatorial de: {numero}")
        print(f"{numero}! = ", end="")
        for i in range(numero, 0, -1):
            print(i, end="")
            if i != 1:
                print(" . ", end="")
        print(f" = {fatorial}")


def main():
    fatorial = F()
    fatorial.calcular_f()


if __name__ == "__main__":
    main()
