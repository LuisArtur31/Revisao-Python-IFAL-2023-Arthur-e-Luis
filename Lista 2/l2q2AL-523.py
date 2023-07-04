#Lista de Exercício 2 - Questão 2
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

class ValorInvalidoException(Exception):
    pass

class VerificadorPositivoNegativo:
    def __init__(self):
        self.valor = None

    def ler_valor(self):
        while True:
            try:
                self.valor = float(input("Digite um valor: "))
                break
            except ValueError:
                print("Valor inválido. Digite um número.")

    def verificar_positivo_negativo(self):
        if self.valor is None:
            raise ValorInvalidoException("Nenhum valor foi informado.")

        if self.valor > 0:
            return "O valor é positivo."
        elif self.valor < 0:
            return "O valor é negativo."
        else:
            return "O valor é zero."


def main():
    verificador = VerificadorPositivoNegativo()

    try:
        verificador.ler_valor()
        resultado = verificador.verificar_positivo_negativo()
        print(resultado)
    except ValorInvalidoException as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
