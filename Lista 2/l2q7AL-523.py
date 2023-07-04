#Lista de Exercício 2 - Questão 7
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia três números e mostre o maior e o menor deles.

class MaiorMenorNumero:
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

    def encontrar_maior(self):
        maior = max(self.num1, self.num2, self.num3)
        return maior

    def encontrar_menor(self):
        menor = min(self.num1, self.num2, self.num3)
        return menor


try:
    numeros = MaiorMenorNumero()
    numeros.solicitar_numeros()
    maior = numeros.encontrar_maior()
    menor = numeros.encontrar_menor()

    print("Maior número:", maior)
    print("Menor número:", menor)

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
