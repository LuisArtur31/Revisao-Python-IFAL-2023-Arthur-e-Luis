#Lista de Exercício 3 - Questão 26
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

class Eleicao:
    def __init__(self):
        self.candidatos = {
            1: {"nome": "Candidato 1", "votos": 0},
            2: {"nome": "Candidato 2", "votos": 0},
            3: {"nome": "Candidato 3", "votos": 0}
        }

    def realizar_votacao(self, total_eleitores):
        for _ in range(total_eleitores):
            try:
                voto = int(input("Digite o número do candidato (1, 2 ou 3): "))
                if voto in self.candidatos:
                    self.candidatos[voto]["votos"] += 1
                else:
                    print("Candidato inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def mostrar_resultado(self):
        for candidato in self.candidatos.values():
            print(f"Candidato: {candidato['nome']} - Votos: {candidato['votos']}")


def main():
    eleicao = Eleicao()

    try:
        total_eleitores = int(input("Digite o número total de eleitores: "))
        eleicao.realizar_votacao(total_eleitores)
        eleicao.mostrar_resultado()
    except ValueError:
        print("Entrada inválida. Digite um número inteiro para o número total de eleitores.")


if __name__ == "__main__":
    main()
