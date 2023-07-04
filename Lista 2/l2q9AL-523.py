#Lista de Exercício 2 - Questão 9
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia três números e mostre-os em ordem decrescente.

class OrdenadorNumeros:
    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.num3 = None

    def solicitar_numeros(self):
        while True:
            try:
                self.num1 = float(input("Digite o primeiro número: "))
                self.num2 = float(input("Digite o segundo número: "))
                self.num3 = float(input("Digite o terceiro número: "))
                break
            except ValueError:
                print("Digite apenas valores numéricos!")

    def ordenar_decrescente(self):
        numeros = [self.num1, self.num2, self.num3]
        numeros.sort(reverse=True)
        return numeros


try:
    ordenador = OrdenadorNumeros()
    ordenador.solicitar_numeros()
    numeros_ordenados = ordenador.ordenar_decrescente()

    print("Números em ordem decrescente:", numeros_ordenados)

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
