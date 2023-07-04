#Lista de Exercício 2 - Questão 19
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

class DecomposicaoNumero:
    def __init__(self, numero):
        self.numero = numero

    def decompor_numero(self):
        if self.numero < 1 or self.numero >= 1000:
            raise ValueError("O número deve ser menor que 1000.")

        centenas = self.numero // 100
        dezenas = (self.numero % 100) // 10
        unidades = self.numero % 10

        return centenas, dezenas, unidades


try:
    numero = int(input("Digite um número inteiro menor que 1000: "))

    decomposicao = DecomposicaoNumero(numero)
    centenas, dezenas, unidades = decomposicao.decompor_numero()

    resultado = ""
    if centenas > 0:
        if centenas == 1:
            resultado += "1 centena"
        else:
            resultado += f"{centenas} centenas"

        if dezenas > 0 or unidades > 0:
            resultado += ", "

    if dezenas > 0:
        if dezenas == 1:
            resultado += "1 dezena"
        else:
            resultado += f"{dezenas} dezenas"

        if unidades > 0:
            resultado += " e "

    if unidades > 0:
        if unidades == 1:
            resultado += "1 unidade"
        else:
            resultado += f"{unidades} unidades"

    print(f"{numero} = {resultado}")
except ValueError as error:
    print(error)
