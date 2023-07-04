#Lista de Exercício 1 - Questão 3
#Dupla: 2020122345 - Arthur Durval e 2020122347 - Luís Artur
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça dois números e imprima a soma.

class Calculadora:
    def solicitar_numero(self):
        try:
            numero = float(input("Digite um número: "))
            return numero
        except ValueError:
            print("Erro: Valor inválido. Por favor, digite um número válido.")
            return None

    def somar(self, numero1, numero2):
        try:
            soma = numero1 + numero2
            return soma
        except Exception as e:
            print("Erro ao calcular a soma:", e)
            return None

def main():
    try:
        calculadora = Calculadora()
        numero1 = calculadora.solicitar_numero()
        numero2 = calculadora.solicitar_numero()

        if numero1 is not None and numero2 is not None:
            resultado = calculadora.somar(numero1, numero2)
            if resultado is not None:
                print("A soma dos números é:", resultado)
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
