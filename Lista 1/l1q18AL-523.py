#Lista de Exercício 1 - Questão 18
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

class ValorInvalidoException(Exception):
    pass


class CalculadoraDownload:
    def __init__(self):
        self.tamanho_arquivo = None
        self.velocidade_internet = None

    def ler_tamanho_arquivo(self):
        while True:
            try:
                self.tamanho_arquivo = float(input("Digite o tamanho do arquivo para download (em MB): "))
                if self.tamanho_arquivo <= 0:
                    raise ValorInvalidoException("Tamanho inválido. Digite um valor positivo.")
                break
            except ValueError:
                print("Valor inválido. Digite um número.")
            except ValorInvalidoException as e:
                print(f"Erro: {str(e)}")

    def ler_velocidade_internet(self):
        while True:
            try:
                self.velocidade_internet = float(input("Digite a velocidade do link de Internet (em Mbps): "))
                if self.velocidade_internet <= 0:
                    raise ValorInvalidoException("Velocidade inválida. Digite um valor positivo.")
                break
            except ValueError:
                print("Valor inválido. Digite um número.")
            except ValorInvalidoException as e:
                print(f"Erro: {str(e)}")

    def calcular_tempo_download(self):
        if self.tamanho_arquivo is None or self.velocidade_internet is None:
            raise ValorInvalidoException("Tamanho do arquivo ou velocidade da Internet não foram informados.")

        tamanho_bits = self.tamanho_arquivo * 8 * 1024 * 1024  # Conversão de MB para bits
        velocidade_bits = self.velocidade_internet * 1024 * 1024  # Conversão de Mbps para bits por segundo

        tempo_segundos = tamanho_bits / velocidade_bits
        tempo_minutos = tempo_segundos / 60

        return tempo_minutos


def main():
    calculadora = CalculadoraDownload()

    try:
        calculadora.ler_tamanho_arquivo()
        calculadora.ler_velocidade_internet()
        tempo_download = calculadora.calcular_tempo_download()
        print(f"Tempo aproximado de download: {tempo_download:.2f} minutos")
    except ValorInvalidoException as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
