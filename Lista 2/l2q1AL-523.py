#Lista de Exercício 2 - Questão 1
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça dois números e imprima o maior deles.

class NumeroMaior:
    def __init__(self):
        self.numero1 = None
        self.numero2 = None

    def solicitar_numeros(self):
        while True:
            try:
                self.numero1 = float(input("Digite o primeiro número: "))
                self.numero2 = float(input("Digite o segundo número: "))
                break
            except ValueError:
                print("Digite apenas valores numéricos!")

    def obter_maior_numero(self):
        if self.numero1 > self.numero2:
            return self.numero1
        elif self.numero2 > self.numero1:
            return self.numero2
        else:
            return None


try:
    numeros = NumeroMaior()
    numeros.solicitar_numeros()
    maior_numero = numeros.obter_maior_numero()

    if maior_numero is not None:
        print("O maior número é:", maior_numero)
    else:
        print("Os números são iguais!")

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
