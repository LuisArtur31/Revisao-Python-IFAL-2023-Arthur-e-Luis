#Lista de Exercício 1 - Questão 4
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

class NotaInvalidaException(Exception):
    pass


class CalculadoraMedia:
    def __init__(self):
        self.notas = []

    def ler_notas(self):
        for i in range(4):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i+1}: "))
                    if nota < 0 or nota > 10:
                        raise NotaInvalidaException("Nota inválida. Digite um valor entre 0 e 10.")
                    self.notas.append(nota)
                    break
                except ValueError:
                    print("Valor inválido. Digite um número.")
                except NotaInvalidaException as e:
                    print(f"Erro: {str(e)}")

    def calcular_media(self):
        if len(self.notas) == 0:
            raise NotaInvalidaException("Nenhuma nota foi informada.")

        soma = sum(self.notas)
        media = soma / len(self.notas)
        return media


def main():
    calculadora = CalculadoraMedia()

    try:
        calculadora.ler_notas()
        media = calculadora.calcular_media()
        print(f"A média das notas é: {media:.2f}")
    except NotaInvalidaException as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
