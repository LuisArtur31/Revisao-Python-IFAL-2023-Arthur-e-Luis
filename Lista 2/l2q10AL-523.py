#Lista de Exercício 2 - Questão 10
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

class TurnoInvalidoException(Exception):
    pass


class TurnoEstudo:
    def __init__(self):
        self.turno = None

    def ler_turno(self):
        while True:
            try:
                self.turno = input("Em qual turno você estuda? (M - Matutino, V - Vespertino, N - Noturno): ")
                if self.turno not in ["M", "V", "N"]:
                    raise TurnoInvalidoException("Valor inválido. Digite M, V ou N.")
                break
            except TurnoInvalidoException as e:
                print(f"Erro: {str(e)}")

    def saudacao(self):
        if self.turno == "M":
            print("Bom Dia!")
        elif self.turno == "V":
            print("Boa Tarde!")
        elif self.turno == "N":
            print("Boa Noite!")


def main():
    turno_estudo = TurnoEstudo()

    turno_estudo.ler_turno()
    turno_estudo.saudacao()


if __name__ == "__main__":
    main()
