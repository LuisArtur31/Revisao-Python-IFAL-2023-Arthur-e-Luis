#Lista de Exercício 3 - Questão 5
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

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
    while True:
        try:
            populacao_a = int(input("Informe a população do país A: "))
            taxa_crescimento_a = float(input("Informe a taxa de crescimento do país A (%): "))
            populacao_b = int(input("Informe a população do país B: "))
            taxa_crescimento_b = float(input("Informe a taxa de crescimento do país B (%): "))

            populacoes = Populacao(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b)
            anos_necessarios = populacoes.calcular_crescimento_populacional()

            print(f"Serão necessários {anos_necessarios} anos para que a população do país A ultrapasse ou iguale a população do país B.")
            break
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar valores numéricos corretos.")

if __name__ == "__main__":
    main()
