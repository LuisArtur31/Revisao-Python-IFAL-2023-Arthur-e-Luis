#Lista de Exercício 3 - Questão 9
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

class NumerosImpares:
    def imprimir_impares(self):
        try:
            for num in range(1, 51):
                if num % 2 != 0:
                    print(num)
        except Exception as e:
            print(f"Ocorreu um erro: {str(e)}")

def main():
    impares = NumerosImpares()
    impares.imprimir_impares()

if __name__ == "__main__":
    main()

