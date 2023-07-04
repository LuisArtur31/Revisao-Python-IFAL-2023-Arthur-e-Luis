#Lista de Exercício 2 - Questão 23
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

class VerificadorNumero:
    def __init__(self, numero):
        self.numero = numero

    def verificar_tipo_numero(self):
        numero_arredondado = round(self.numero)
        if numero_arredondado == self.numero:
            return "inteiro"
        else:
            return "decimal"


try:
    numero = float(input("Digite um número: "))

    verificador = VerificadorNumero(numero)

    tipo_numero = verificador.verificar_tipo_numero()

    print(f"O número {numero} é do tipo {tipo_numero}.")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número válido.")
