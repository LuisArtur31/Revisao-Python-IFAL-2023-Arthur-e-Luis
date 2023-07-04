#Lista de Exercício 7 - Questão 11
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

#Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
#O consumo é especificado no construtor e o nível de combustível inicial é 0.
#Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
#Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
#Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
#meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
#meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
#meuFusca.andar(100);            # anda 100 quilômetros.
#meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.

class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, distancia):
        consumo_total = distancia / self.consumo
        if consumo_total <= self.combustivel:
            self.combustivel -= consumo_total
            print(f"O carro percorreu {distancia} km.")
        else:
            print("Combustível insuficiente. O carro não pode percorrer a distância especificada.")

    def obterGasolina(self):
        return self.combustivel

    def adicionarGasolina(self, quantidade):
        if quantidade >= 0:
            self.combustivel += quantidade
            print(f"Foram adicionados {quantidade} litros de combustível ao tanque.")
        else:
            print("A quantidade de combustível adicionada deve ser um valor positivo.")


# Exemplo de uso:
meuFusca = Carro(15)            # 15 quilômetros por litro de combustível.
meuFusca.adicionarGasolina(20)  # abastece com 20 litros de combustível.
meuFusca.andar(100)             # anda 100 quilômetros.
print("Combustível restante:", meuFusca.obterGasolina())  # Imprime o combustível que resta no tanque.
