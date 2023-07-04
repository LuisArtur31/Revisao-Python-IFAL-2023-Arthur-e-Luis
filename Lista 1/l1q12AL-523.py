#Lista de Exercício 1 - Questão 12
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

class AlturaInvalidaException(Exception):
    pass

class CalculadoraPesoIdeal:
    def __init__(self):
        self.altura = None

    def ler_altura(self):
        while True:
            try:
                self.altura = float(input("Digite a altura da pessoa (em metros): "))
                if self.altura <= 0:
                    raise AlturaInvalidaException("Altura inválida. Digite um valor positivo.")
                break
            except ValueError:
                print("Valor inválido. Digite um número.")
            except AlturaInvalidaException as e:
                print(f"Erro: {str(e)}")

    def calcular_peso_ideal(self):
        if self.altura is None:
            raise AlturaInvalidaException("Nenhuma altura foi informada.")

        peso_ideal = (72.7 * self.altura) - 58
        return peso_ideal


def main():
    calculadora = CalculadoraPesoIdeal()

    try:
        calculadora.ler_altura()
        peso_ideal = calculadora.calcular_peso_ideal()
        print(f"O peso ideal da pessoa é: {peso_ideal:.2f} kg")
    except AlturaInvalidaException as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
