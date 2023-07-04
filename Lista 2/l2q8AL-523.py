#Lista de Exercício 2 - Questão 8
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

class ValorInvalidoException(Exception):
    pass


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"


class DecisorCompra:
    def __init__(self):
        self.produtos = []

    def ler_precos(self):
        for i in range(3):
            while True:
                try:
                    nome = input(f"Digite o nome do produto {i+1}: ")
                    preco = float(input(f"Digite o preço do produto {i+1}: "))
                    if preco < 0:
                        raise ValorInvalidoException("O preço não pode ser negativo.")
                    produto = Produto(nome, preco)
                    self.produtos.append(produto)
                    break
                except ValueError:
                    print("Valor inválido. Digite um número.")

    def encontrar_menor_preco(self):
        if not self.produtos:
            raise ValorInvalidoException("Nenhum produto foi informado.")

        menor_preco = min(self.produtos, key=lambda produto: produto.preco)
        return menor_preco


def main():
    decisor = DecisorCompra()

    try:
        decisor.ler_precos()
        produto_mais_barato = decisor.encontrar_menor_preco()
        print(f"Você deve comprar o produto mais barato:\n{produto_mais_barato}")
    except ValorInvalidoException as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
