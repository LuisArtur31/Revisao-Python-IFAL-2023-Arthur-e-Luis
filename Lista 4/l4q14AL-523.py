#Lista de Exercício 4 - Questão 14
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

class ClassificadorC:
    def __init__(self):
        self.respostas = []

    def fazer_p(self):
        perguntas = [
            "Telefonou para a vítima?",
            "Esteve no local do crime?",
            "Mora perto da vítima?",
            "Devia para a vítima?",
            "Já trabalhou com a vítima?"
        ]

        for pergunta in perguntas:
            resposta = input(pergunta + " (S/N): ").upper()
            while resposta != "S" and resposta != "N":
                resposta = input("Resposta inválida. Digite S para Sim ou N para Não: ").upper()
            self.respostas.append(resposta)

    def classificar_p(self):
        positivas = self.respostas.count("S")

        if positivas == 2:
            return "Suspeita"
        elif 3 <= positivas <= 4:
            return "Cúmplice"
        elif positivas == 5:
            return "Assassino"
        else:
            return "Inocente"


try:
    classificador = ClassificadorC()

    classificador.fazer_p()

    classificacao = classificador.classificar_p()

    print(f"Classificação: {classificacao}")
except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")


