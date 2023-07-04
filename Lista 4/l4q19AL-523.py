#Lista de Exercício 4 - Questão 19
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

#As possíveis respostas são:

#1- Windows Server
#2- Unix
#3- Linux
#4- Netware
#5- Mac OS
#6- Outro
#Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
#Sistema Operacional     Votos   %
#-------------------     -----   ---
#Windows Server           1500   17%
#Unix                     3500   40%
#Linux                    3000   34%
#Netware                   500    5%
#Mac OS                    150    2%
#Outro                     150    2%
#-------------------     -----
#Total                    8800

#O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

class Enquete:
    def __init__(self):
        self.opcoes = {
            1: "Windows Server",
            2: "Unix",
            3: "Linux",
            4: "Netware",
            5: "Mac OS",
            6: "Outro"
        }
        self.votos = [0] * len(self.opcoes)

    def adicionar_voto(self, opcao):
        self.votos[opcao - 1] += 1

    def calcular_percentual(self, total_votos):
        percentuais = []
        for voto in self.votos:
            percentual = (voto / total_votos) * 100
            percentuais.append(percentual)
        return percentuais

    def mostrar_resultado(self):
        total_votos = sum(self.votos)

        print("Sistema Operacional     Votos   %")
        print("-------------------     -----   ---")
        for i, voto in enumerate(self.votos):
            sistema = self.opcoes[i + 1]
            percentual = self.calcular_percentual(total_votos)[i]
            print(f"{sistema:<25} {voto:<7} {percentual:.1f}%")
        print("-------------------     -----   ---")
        print(f"Total                    {total_votos}")


def main():
    enquete = Enquete()

    while True:
        try:
            voto = int(input("Informe o número da opção desejada (0 para encerrar): "))
            if voto == 0:
                break
            if voto < 0 or voto > 6:
                raise ValueError("Opção inválida.")
            enquete.adicionar_voto(voto)
        except ValueError as e:
            print("Erro:", str(e))

    enquete.mostrar_resultado()


if __name__ == "__main__":
    main()
