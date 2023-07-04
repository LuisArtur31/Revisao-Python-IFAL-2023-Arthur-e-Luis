#Lista de Exercício 3 - Questão 47
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
#Atleta: Aparecido Parente
#Nota: 9.9
#Nota: 7.5
#Nota: 9.5
#Nota: 8.5
#Nota: 9.0
#Nota: 8.5
#Nota: 9.7

#Resultado final:
#Atleta: Aparecido Parente
#Melhor nota: 9.9
#Pior nota: 7.5
#Média: 9,04

class Ginasta:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        notas_ordenadas = sorted(self.notas)
        notas_ordenadas = notas_ordenadas[1:-1] 
        media = sum(notas_ordenadas) / len(notas_ordenadas)
        return media


def main():
    nome_ginasta = input("Digite o nome do ginasta: ")
    ginasta = Ginasta(nome_ginasta)

    for i in range(1, 8):
        while True:
            try:
                nota = float(input(f"Nota {i}: "))
                break
            except ValueError:
                print("Valor inválido. Digite um número.")

        ginasta.adicionar_nota(nota)

    media = ginasta.calcular_media()

    print("\nResultado final:")
    print(f"Atleta: {ginasta.nome}")
    print(f"Melhor nota: {max(ginasta.notas)}")
    print(f"Pior nota: {min(ginasta.notas)}")
    print(f"Média: {media:.2f}")


if __name__ == "__main__":
    main()
