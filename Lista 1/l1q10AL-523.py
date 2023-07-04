#Lista de Exercício 1 - Questão 10
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

class TemperaturaInvalidaException(Exception):
    pass


class ConversorTemperatura:
    def __init__(self):
        self.temperatura_celsius = None

    def ler_temperatura(self):
        while True:
            try:
                self.temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
                break
            except ValueError:
                print("Valor inválido. Digite um número.")

    def converter_fahrenheit(self):
        if self.temperatura_celsius is None:
            raise TemperaturaInvalidaException("Nenhuma temperatura foi informada.")

        temperatura_fahrenheit = (self.temperatura_celsius * 9/5) + 32
        return temperatura_fahrenheit


def main():
    conversor = ConversorTemperatura()

    try:
        conversor.ler_temperatura()
        temperatura_fahrenheit = conversor.converter_fahrenheit()
        print(f"A temperatura em graus Fahrenheit é: {temperatura_fahrenheit:.2f}°F")
    except TemperaturaInvalidaException as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
