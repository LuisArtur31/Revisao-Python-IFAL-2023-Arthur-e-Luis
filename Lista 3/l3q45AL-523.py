#Lista de Exercício 3 - Questão 45
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
#Maior e Menor Acerto;
#Total de Alunos que utilizaram o sistema;
#A Média das Notas da Turma.
#Gabarito da Prova:

#01 - A
#02 - B
#03 - C
#04 - D
#05 - E
#06 - E
#07 - D
#08 - C
#09 - B
#10 - A
#Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.respostas = []

    def responder_questao(self, resposta):
        self.respostas.append(resposta)


class Prova:
    def __init__(self):
        self.gabarito = []

    def definir_gabarito(self):
        print("Defina o gabarito da prova:")
        for i in range(1, 11):
            while True:
                try:
                    resposta = input(f"Resposta da questão {i}: ").upper()
                    if resposta not in ['A', 'B', 'C', 'D', 'E']:
                        raise ValueError("Resposta inválida. Digite A, B, C, D ou E.")
                    break
                except ValueError as e:
                    print(f"Erro: {e}")
        self.gabarito.append(resposta)

    def corrigir_prova(self, alunos):
        resultados = []
        for aluno in alunos:
            acertos = sum([1 for r, g in zip(aluno.respostas, self.gabarito) if r == g])
            resultados.append(acertos)

        return resultados


def main():
    prova = Prova()
    prova.definir_gabarito()

    alunos = []
    continuar = True

    while continuar:
        nome_aluno = input("\nDigite o nome do aluno: ")

        aluno = Aluno(nome_aluno)

        print(f"\nRespostas do aluno {aluno.nome}:")
        for i in range(1, 11):
            while True:
                try:
                    resposta = input(f"Resposta da questão {i}: ").upper()
                    if resposta not in ['A', 'B', 'C', 'D', 'E']:
                        raise ValueError("Resposta inválida. Digite A, B, C, D ou E.")
                    break
                except ValueError as e:
                    print(f"Erro: {e}")

            aluno.responder_questao(resposta)

        alunos.append(aluno)

        while True:
            try:
                opcao = input("\nDeseja continuar? (S/N) ").upper()
                if opcao not in ['S', 'N']:
                    raise ValueError("Opção inválida. Digite S ou N.")
                break
            except ValueError as e:
                print(f"Erro: {e}")

        if opcao == "N":
            continuar = False

    resultados = prova.corrigir_prova(alunos)

    maior_acerto = max(resultados)
    menor_acerto = min(resultados)
    total_alunos = len(alunos)
    media_notas = sum(resultados) / total_alunos

    print("\n----- Resultados -----\n")
    print(f"Maior acerto: {maior_acerto} questões")
    print(f"Menor acerto: {menor_acerto} questões")
    print(f"Total de alunos: {total_alunos}")
    print(f"Média das notas: {media_notas:.2f}")


if __name__ == "__main__":
    main()
