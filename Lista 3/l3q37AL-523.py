#Lista de Exercício 3 - Questão 37
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.

class Cliente:
    def __init__(self, codigo, altura, peso):
        self.codigo = codigo
        self.altura = altura
        self.peso = peso

    def __str__(self):
        return f"Código: {self.codigo}, Altura: {self.altura}m, Peso: {self.peso}kg"


class Academia:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self):
        while True:
            try:
                codigo = int(input("Digite o código do cliente (digite 0 para encerrar): "))
                if codigo == 0:
                    break
                altura = float(input("Digite a altura do cliente (em metros): "))
                peso = float(input("Digite o peso do cliente (em kg): "))
                cliente = Cliente(codigo, altura, peso)
                self.clientes.append(cliente)
            except ValueError:
                print("Valor inválido. Digite um número inteiro para o código e números reais para a altura e o peso.")

    def obter_mais_alto(self):
        if not self.clientes:
            return None
        mais_alto = max(self.clientes, key=lambda x: x.altura)
        return mais_alto

    def obter_mais_baixo(self):
        if not self.clientes:
            return None
        mais_baixo = min(self.clientes, key=lambda x: x.altura)
        return mais_baixo

    def obter_mais_gordo(self):
        if not self.clientes:
            return None
        mais_gordo = max(self.clientes, key=lambda x: x.peso)
        return mais_gordo

    def obter_mais_magro(self):
        if not self.clientes:
            return None
        mais_magro = min(self.clientes, key=lambda x: x.peso)
        return mais_magro

    def calcular_media_altura(self):
        if not self.clientes:
            return 0
        soma_altura = sum(cliente.altura for cliente in self.clientes)
        return soma_altura / len(self.clientes)

    def calcular_media_peso(self):
        if not self.clientes:
            return 0
        soma_peso = sum(cliente.peso for cliente in self.clientes)
        return soma_peso / len(self.clientes)

    def exibir_resultados(self):
        print("Clientes cadastrados:")
        for cliente in self.clientes:
            print(cliente)
        print()

        mais_alto = self.obter_mais_alto()
        if mais_alto:
            print("Cliente mais alto:")
            print(mais_alto)
        else:
            print("Nenhum cliente cadastrado.")
        print()

        mais_baixo = self.obter_mais_baixo()
        if mais_baixo:
            print("Cliente mais baixo:")
            print(mais_baixo)
        else:
            print("Nenhum cliente cadastrado.")
        print()

        mais_gordo = self.obter_mais_gordo()
        if mais_gordo:
            print("Cliente mais gordo:")
            print(mais_gordo)
        else:
            print("Nenhum cliente cadastrado.")
        print()

        mais_magro = self.obter_mais_magro()
        if mais_magro:
            print("Cliente mais magro:")
            print(mais_magro)
        else:
            print("Nenhum cliente cadastrado.")
        print()

        media_altura = self.calcular_media_altura()
        media_peso = self.calcular_media_peso()
        print(f"Média das alturas: {media_altura:.2f}m")
        print(f"Média dos pesos: {media_peso:.2f}kg")


def main():
    academia = Academia()
    academia.cadastrar_cliente()
    academia.exibir_resultados()


if __name__ == "__main__":
    main()



