#Lista de Exercício 3 - Questão 25
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

class Turma:
    def __init__(self):
        self.idades = []

    def ler_idades(self, n):
        for i in range(n):
            while True:
                try:
                    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
                    if idade < 0:
                        raise ValueError
                    self.idades.append(idade)
                    break
                except ValueError:
                    print("Valor inválido. Digite uma idade válida.")

    def calcular_media_idades(self):
        if not self.idades:
            return None
        return sum(self.idades) / len(self.idades)

    def classificar_turma(self):
        media = self.calcular_media_idades()
        if media is None:
            return None
        elif media >= 0 and media <= 25:
            return "Jovem"
        elif media >= 26 and media <= 60:
            return "Adulta"
        else:
            return "Idosa"


def main():
    turma = Turma()

    while True:
        try:
            n = int(input("Digite a quantidade de pessoas na turma: "))
            if n < 1:
                raise ValueError
            break
        except ValueError:
            print("Valor inválido. Digite um número inteiro positivo.")

    turma.ler_idades(n)

    media_idades = turma.calcular_media_idades()
    classificacao = turma.classificar_turma()

    if media_idades is not None:
        print(f"Média de idades da turma: {media_idades:.2f}")
        if classificacao is not None:
            print(f"Classificação da turma: {classificacao}")
        else:
            print("Não há pessoas na turma.")
    else:
        print("Não há pessoas na turma.")


if __name__ == "__main__":
    main()
