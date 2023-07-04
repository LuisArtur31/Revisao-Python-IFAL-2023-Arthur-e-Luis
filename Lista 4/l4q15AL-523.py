#Lista de Exercício 4 - Questão 15
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;

class Notas:
    def __init__(self):
        self.notas = []

    def ler_notas(self):
        while True:
            try:
                nota = float(input("Digite uma nota (-1 para encerrar): "))
                if nota == -1:
                    break
                self.notas.append(nota)
            except ValueError:
                print("Valor inválido. Digite um número.")

    def mostrar_quantidade_notas(self):
        quantidade = len(self.notas)
        print(f"Quantidade de valores lidos: {quantidade}")

    def mostrar_notas_ordem_original(self):
        print("Valores na ordem original:")
        for nota in self.notas:
            print(nota, end=" ")

    def mostrar_notas_ordem_inversa(self):
        print("\nValores na ordem inversa:")
        for nota in reversed(self.notas):
            print(nota)

    def calcular_soma(self):
        soma = sum(self.notas)
        return soma

    def calcular_media(self):
        media = sum(self.notas) / len(self.notas)
        return media

    def mostrar_notas_acima_media(self, media):
        notas_acima_media = [nota for nota in self.notas if nota > media]
        quantidade_acima_media = len(notas_acima_media)
        print(f"Quantidade de valores acima da média: {quantidade_acima_media}")

    def mostrar_notas_abaixo_sete(self):
        notas_abaixo_sete = [nota for nota in self.notas if nota < 7]
        quantidade_abaixo_sete = len(notas_abaixo_sete)
        print(f"Quantidade de valores abaixo de sete: {quantidade_abaixo_sete}")

    @staticmethod
    def encerrar_programa():
        print("Programa encerrado.")


def main():
    notas = Notas()
    notas.ler_notas()
    notas.mostrar_quantidade_notas()
    notas.mostrar_notas_ordem_original()
    notas.mostrar_notas_ordem_inversa()
    soma = notas.calcular_soma()
    media = notas.calcular_media()
    notas.mostrar_notas_acima_media(media)
    notas.mostrar_notas_abaixo_sete()
    notas.encerrar_programa()


if __name__ == "__main__":
    main()
