#Lista de Exercício 4 - Questão 22
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
#Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
#necessita da esfera;
#necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
#Quantidade de mouses: 100

#Situação                        Quantidade              Percentual
#1- necessita da esfera                  40                     40%
#2- necessita de limpeza                 30                     30%
#3- necessita troca do cabo ou conector  15                     15%
#4- quebrado ou inutilizado              15                     15%

class Mouse:
    def __init__(self, identificacao, situacao):
        self.identificacao = identificacao
        self.situacao = situacao

    def __str__(self):
        return f"{self.identificacao} - {self.situacao}"


class LevantamentoMouses:
    def __init__(self):
        self.mouses = []

    def adicionar_mouse(self, mouse):
        self.mouses.append(mouse)

    def gerar_relatorio(self):
        situacoes = {
            1: "necessita da esfera",
            2: "necessita de limpeza",
            3: "necessita troca do cabo ou conector",
            4: "quebrado ou inutilizado"
        }

        quantidade_mouses = len(self.mouses)

        print("\nRelatório de Levantamento de Sucatas de Mouses")
        print("==============================================\n")
        print("Quantidade de mouses: ", quantidade_mouses)
        print("\nSituação                        Quantidade              Percentual")

        for situacao_id, situacao_nome in situacoes.items():
            quantidade = sum(1 for mouse in self.mouses if mouse.situacao == situacao_id)
            percentual = (quantidade / quantidade_mouses) * 100
            print(f"{situacao_id}- {situacao_nome:<30}{quantidade:<24}{percentual:.1f}%")

        print()


def main():
    levantamento = LevantamentoMouses()

    while True:
        try:
            identificacao = int(input("Número de identificação do mouse (0 para encerrar): "))

            if identificacao == 0:
                break

            if identificacao < 0:
                print("Identificação inválida. Digite um número não negativo.")
                continue

            situacao = int(input("Tipo de defeito (1 - necessita da esfera, 2 - necessita de limpeza, 3 - necessita troca do cabo ou conector, 4 - quebrado ou inutilizado): "))

            if situacao not in range(1, 5):
                print("Situação inválida. Digite um número válido.")
                continue

            mouse = Mouse(identificacao, situacao)
            levantamento.adicionar_mouse(mouse)

        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    levantamento.gerar_relatorio()


if __name__ == "__main__":
    main()
