#Lista de Exercício 1 - Questão 9
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

class ConversorTemperatura:
    def solicitar_temperatura(self):
        try:
            temperatura = float(input("Digite a temperatura em graus Fahrenheit: "))
            return temperatura
        except ValueError:
            print("Erro: Valor inválido. Por favor, digite um número válido.")
            return None

    def converter_para_celsius(self, temperatura):
        try:
            celsius = (temperatura - 32) * 5 / 9
            return celsius
        except Exception as e:
            print("Erro ao converter para Celsius:", e)
            return None

def main():
    try:
        conversor = ConversorTemperatura()
        temperatura_fahrenheit = conversor.solicitar_temperatura()

        if temperatura_fahrenheit is not None:
            temperatura_celsius = conversor.converter_para_celsius(temperatura_fahrenheit)
            if temperatura_celsius is not None:
                print(f"A temperatura em graus Celsius é: {temperatura_celsius:.2f} °C")
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
