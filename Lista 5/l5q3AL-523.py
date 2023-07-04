#Lista de Exercício 5 - Questão 3
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

class SomaArgumentos:
    def soma_tres_argumentos(self, arg1, arg2, arg3):
        return arg1 + arg2 + arg3

def main():
    try:
        arg1 = int(input("Digite o primeiro argumento: "))
        arg2 = int(input("Digite o segundo argumento: "))
        arg3 = int(input("Digite o terceiro argumento: "))

        soma = SomaArgumentos()
        resultado = soma.soma_tres_argumentos(arg1, arg2, arg3)
        print("A soma dos argumentos é:", resultado)

    except ValueError:
        print("Erro: Digite apenas valores numéricos.")

if __name__ == "__main__":
    main()
