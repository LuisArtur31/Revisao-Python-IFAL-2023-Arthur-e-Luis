#Lista de Exercício 3 - Questão 28
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

class ColecaoCDs:
    def __init__(self):
        self.quantidade_cds = 0
        self.valor_total = 0

    def calcular_valor_total(self):
        try:
            self.quantidade_cds = int(input("Digite a quantidade de CDs na coleção: "))
            if self.quantidade_cds <= 0:
                raise ValueError("A quantidade de CDs deve ser um número positivo.")

            for i in range(1, self.quantidade_cds + 1):
                valor_cd = float(input(f"Digite o valor do CD {i}: "))
                if valor_cd <= 0:
                    raise ValueError(f"O valor do CD {i} deve ser um número positivo.")
                self.valor_total += valor_cd

        except ValueError as e:
            print(f"Entrada inválida: {e}")
            return

        self.calcular_valor_medio()

    def calcular_valor_medio(self):
        valor_medio = self.valor_total / self.quantidade_cds
        print(f"Valor total investido: R$ {self.valor_total:.2f}")
        print(f"Valor médio gasto em cada CD: R$ {valor_medio:.2f}")


def main():
    colecao_cds = ColecaoCDs()
    colecao_cds.calcular_valor_total()


if __name__ == "__main__":
    main()
