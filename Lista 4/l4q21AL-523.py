#Lista de Exercício 4 - Questão 21
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
#O modelo do carro mais econômico;
#Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
#Comparativo de Consumo de Combustível

#Veículo 1
#Nome: fusca
#Km por litro: 7
#Veículo 2
#Nome: gol
#Km por litro: 10
#Veículo 3
#Nome: uno
#Km por litro: 12.5
#Veículo 4
#Nome: Vectra
#Km por litro: 9
#eículo 5
#Nome: Peugeout
#Km por litro: 14.5

#Relatório Final
# 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
# 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
# 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
# 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
# 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
#O menor consumo é do peugeout.

class Carro:
    def __init__(self, modelo, consumo):
        self.modelo = modelo
        self.consumo = consumo

    def calcular_litros(self, distancia):
        return distancia / self.consumo

    def calcular_custo(self, distancia, preco_combustivel):
        litros = self.calcular_litros(distancia)
        custo = litros * preco_combustivel
        return custo


def main():
    carros = []
    precos_combustivel = 2.25

    try:
        for i in range(5):
            modelo = input(f"Digite o modelo do carro {i+1}: ")
            consumo = float(input(f"Digite o consumo do carro {i+1} (km por litro): "))
            carros.append(Carro(modelo, consumo))
    except ValueError:
        print("Valor inválido. Certifique-se de digitar um número para o consumo.")

    print("\nComparativo de Consumo de Combustível\n")

    for i, carro in enumerate(carros):
        litros = carro.calcular_litros(1000)
        custo = carro.calcular_custo(1000, precos_combustivel)
        print(f"{i+1} - {carro.modelo:<15} - {carro.consumo:<5.1f} - {litros:.1f} litros - R$ {custo:.2f}")

    try:
        maior_consumo_carro = max(carros, key=lambda x: x.consumo)
        print(f"\nO carro com o menor consumo é o {maior_consumo_carro.modelo}.")
    except ValueError:
        print("Não foi possível determinar o carro com o menor consumo.")

if __name__ == "__main__":
    main()
