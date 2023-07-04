#Lista de Exercício 5 - Questão 4
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

class Verificador:
    def verificar_positivo(self, numero):
        if numero > 0:
            return 'P'
        else:
            return 'N'

def main():
    try:
        argumento = float(input("Digite um número: "))

        verificador = Verificador()
        resultado = verificador.verificar_positivo(argumento)
        print("Resultado:", resultado)

    except ValueError:
        print("Erro: Digite um número válido.")

if __name__ == "__main__":
    main()
