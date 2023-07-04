#Lista de Exercício 3 - Questão 44
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
#1 , 2, 3, 4  - Votos para os respectivos candidatos 
#(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#5 - Voto Nulo
#6 - Voto em Branco
#Faça um programa que calcule e mostre:
#O total de votos para cada candidato;
#O total de votos nulos;
#O total de votos em branco;
#A percentagem de votos nulos sobre o total de votos;
#A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

class Eleicao:
    def __init__(self):
        self.candidatos = {
            1: 'José',
            2: 'João',
            3: 'Maria',
            4: 'Ana'
        }
        self.votos_candidatos = {candidato: 0 for candidato in self.candidatos.values()}
        self.votos_nulos = 0
        self.votos_em_branco = 0

    def votar(self, codigo):
        if codigo in self.candidatos:
            self.votos_candidatos[self.candidatos[codigo]] += 1
        elif codigo == 5:
            self.votos_nulos += 1
        elif codigo == 6:
            self.votos_em_branco += 1

    def calcular_percentagem(self, votos, total):
        if total > 0:
            return (votos / total) * 100
        else:
            return 0

    def exibir_resultados(self):
        total_votos = sum(self.votos_candidatos.values()) + self.votos_nulos + self.votos_em_branco

        print("Resultado da Eleição")
        print("=====================")
        print("Candidatos:")
        for candidato, votos in self.votos_candidatos.items():
            print(f"{candidato}: {votos} votos")

        print(f"Nulos: {self.votos_nulos} votos")
        print(f"Branco: {self.votos_em_branco} votos")
        print("=====================")
        print(f"Percentagem de votos nulos: {self.calcular_percentagem(self.votos_nulos, total_votos):.2f}%")
        print(f"Percentagem de votos em branco: {self.calcular_percentagem(self.votos_em_branco, total_votos):.2f}%")

    def realizar_eleicao(self):
        while True:
            codigo = int(input("Digite o código do candidato (ou 0 para encerrar a eleição): "))
            if codigo == 0:
                break
            self.votar(codigo)

        self.exibir_resultados()


eleicao = Eleicao()
eleicao.realizar_eleicao()
