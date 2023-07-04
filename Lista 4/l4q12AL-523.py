#Lista de Exercício 4 - Questão 12
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

class Aluno:
    def __init__(self, idade, altura):
        self.idade = idade
        self.altura = altura

def calcular_media_alturas(alunos):
    soma_alturas = sum(aluno.altura for aluno in alunos)
    media_alturas = soma_alturas / len(alunos)
    return media_alturas

def contar_alunos_inferiores_media(alunos, media_alturas):
    contador = 0
    for aluno in alunos:
        if aluno.idade > 13 and aluno.altura < media_alturas:
            contador += 1
    return contador

def main():
    alunos = []
    for _ in range(30):
        idade = int(input("Informe a idade do aluno: "))
        altura = float(input("Informe a altura do aluno: "))
        alunos.append(Aluno(idade, altura))
    
    media_alturas = calcular_media_alturas(alunos)
    alunos_inferiores_media = contar_alunos_inferiores_media(alunos, media_alturas)
    
    print("Alunos com mais de 13 anos e altura inferior à média: ", alunos_inferiores_media)

if __name__ == "__main__":
    main()
