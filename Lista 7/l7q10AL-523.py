#Lista de Exercício 7 - Questão 10
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

#Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
#tipoCombustivel.
#valorLitro
#quantidadeCombustivel
#Possua no mínimo esses métodos:
#abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
#abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
#alterarValor( ) – altera o valor do litro do combustível.
#alterarCombustivel( ) – altera o tipo do combustível.
#alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
#OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros = valor / self.valorLitro
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            return litros
        else:
            return 0

    def abastecerPorLitro(self, litros):
        valor = litros * self.valorLitro
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            return valor
        else:
            return 0

    def alterarValor(self, novoValor):
        self.valorLitro = novoValor

    def alterarCombustivel(self, novoCombustivel):
        self.tipoCombustivel = novoCombustivel

    def alterarQuantidadeCombustivel(self, novaQuantidade):
        self.quantidadeCombustivel = novaQuantidade

# Exemplo de uso da classe BombaCombustivel
bomba = BombaCombustivel("Gasolina", 4.0, 1000)

print("Quantidade de combustível inicial na bomba:", bomba.quantidadeCombustivel)

litros_abastecidos = bomba.abastecerPorValor(50)
print("Litros abastecidos:", litros_abastecidos)
print("Quantidade de combustível restante na bomba:", bomba.quantidadeCombustivel)

valor_pago = bomba.abastecerPorLitro(10)
print("Valor pago:", valor_pago)
print("Quantidade de combustível restante na bomba:", bomba.quantidadeCombustivel)

bomba.alterarValor(4.5)
bomba.alterarCombustivel("Etanol")
bomba.alterarQuantidadeCombustivel(800)

print("Tipo de combustível:", bomba.tipoCombustivel)
print("Valor do litro:", bomba.valorLitro)
print("Quantidade de combustível na bomba:", bomba.quantidadeCombustivel)
