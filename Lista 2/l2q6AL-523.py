#Lista de Exercício 2 - Questão 6
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia três números e mostre o maior deles

class ValorInvalidoException(Exception):
    pass


class MaiorNumero:
    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.num3 = None

    def ler_numeros(self):
        while True:
            try:
                self.num1 = float(input("Digite o primeiro número: "))
                self.num2 = float(input("Digite o segundo número: "))
                self.num3 = float(input("Digite o terceiro número: "))
                break
            except ValueError:
                print("Valor inválido. Digite um número.")

    def encontrar_maior_numero(self):
        if self.num1 is None or self.num2 is None or self.num3 is None:
            raise ValorInvalidoException("Nem todos os números foram informados.")

        maior = max(self.num1, self.num2, self.num3)
        return maior


def main():
    maior_numero = MaiorNumero()

    try:
        maior_numero.ler_numeros()
        resultado = maior_numero.encontrar_maior_numero()
        print(f"O maior número é: {resultado}")
    except ValorInvalidoException as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
