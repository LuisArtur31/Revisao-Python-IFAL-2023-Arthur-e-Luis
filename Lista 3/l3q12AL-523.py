#Lista de Exercício 3 - Questão 12
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
#...
#5 X 10 = 50

class Tabuada:
    def __init__(self):
        self.numero = 0

    def ler_numero(self):
        while True:
            try:
                self.numero = int(input("Digite um número inteiro entre 1 e 10: "))
                if self.numero < 1 or self.numero > 10:
                    raise ValueError
                break
            except ValueError:
                print("Valor inválido. Digite um número inteiro válido entre 1 e 10.")

    def gerar_tabuada(self):
        print(f"Tabuada de {self.numero}:")
        for i in range(1, 11):
            resultado = self.numero * i
            print(f"{self.numero} X {i} = {resultado}")


def main():
    tabuada = Tabuada()
    tabuada.ler_numero()
    tabuada.gerar_tabuada()


if __name__ == "__main__":
    main()
