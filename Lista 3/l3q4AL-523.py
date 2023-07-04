#Lista de Exercício 3 - Questão 4
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

class Populacao:
    def __init__(self, populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b):
        self.populacao_a = populacao_a
        self.taxa_crescimento_a = taxa_crescimento_a
        self.populacao_b = populacao_b
        self.taxa_crescimento_b = taxa_crescimento_b

    def calcular_crescimento_populacional(self):
        anos = 0
        while self.populacao_a < self.populacao_b:
            self.populacao_a *= (1 + self.taxa_crescimento_a / 100)
            self.populacao_b *= (1 + self.taxa_crescimento_b / 100)
            anos += 1
        return anos

def main():
    populacao_a = 80000
    taxa_crescimento_a = 3
    populacao_b = 200000
    taxa_crescimento_b = 1.5

    populacoes = Populacao(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b)
    anos_necessarios = populacoes.calcular_crescimento_populacional()

    print(f"Serão necessários {anos_necessarios} anos para que a população do país A ultrapasse ou iguale a população do país B.")


if __name__ == "__main__":
    main()
