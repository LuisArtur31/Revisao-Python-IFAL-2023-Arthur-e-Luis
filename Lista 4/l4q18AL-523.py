#Lista de Exercício 4 - Questão 18
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
#O total de votos computados;
#Os númeos e respectivos votos de todos os jogadores que receberam votos;
#O percentual de votos de cada um destes jogadores;
#O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
#Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
#Enquete: Quem foi o melhor jogador?

#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 10
#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 10
#Número do jogador (0=fim): 11
#Número do jogador (0=fim): 10
#Número do jogador (0=fim): 50
#Informe um valor entre 1 e 23 ou 0 para sair!
#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 0

#Resultado da votação:

#Foram computados 8 votos.

#Jogador Votos           %
#9               4               50,0%
#10              3               37,5%
#11              1               12,5%
#O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.

class EnqueteTelevisao:
    def __init__(self):
        self.votos_jogadores = [0] * 24

    def computar_voto(self, numero_jogador):
        if numero_jogador >= 1 and numero_jogador <= 23:
            self.votos_jogadores[numero_jogador] += 1
        else:
            print("Número de jogador inválido. Voto não computado.")

    def calcular_percentual(self, votos_jogador, total_votos):
        return (votos_jogador / total_votos) * 100

    def exibir_resultados(self):
        print("\nResultado da votação:\n")
        total_votos = sum(self.votos_jogadores)
        print(f"Foram computados {total_votos} votos.\n")
        print("Jogador\tVotos\t\t%")
        for jogador, votos in enumerate(self.votos_jogadores):
            if votos > 0:
                percentual = self.calcular_percentual(votos, total_votos)
                print(f"{jogador}\t\t{votos}\t\t{percentual:.1f}%")

        melhor_jogador = self.votos_jogadores.index(max(self.votos_jogadores))
        percentual_melhor = self.calcular_percentual(self.votos_jogadores[melhor_jogador], total_votos)
        print(f"\nO melhor jogador foi o número {melhor_jogador}, com {self.votos_jogadores[melhor_jogador]} votos, correspondendo a {percentual_melhor:.1f}% do total de votos.")

    def gravar_resultados(self):
        with open("resultados.txt", "w") as arquivo:
            arquivo.write("Resultado da votação:\n\n")
            total_votos = sum(self.votos_jogadores)
            arquivo.write(f"Foram computados {total_votos} votos.\n\n")
            arquivo.write("Jogador\tVotos\t\t%\n")
            for jogador, votos in enumerate(self.votos_jogadores):
                if votos > 0:
                    percentual = self.calcular_percentual(votos, total_votos)
                    arquivo.write(f"{jogador}\t\t{votos}\t\t{percentual:.1f}%\n")

def main():
    enquete = EnqueteTelevisao()
    while True:
        try:
            voto = int(input("Número do jogador (0=fim): "))
            if voto == 0:
                break
            enquete.computar_voto(voto)
        except ValueError:
            print("Valor inválido. Informe um número válido ou 0 para sair.")

    enquete.exibir_resultados()
    enquete.gravar_resultados()

if __name__ == "__main__":
    main()
