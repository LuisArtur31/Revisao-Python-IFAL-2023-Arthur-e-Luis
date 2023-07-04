#Lista de Exercício 3 - Questão 6
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

class Numeros:
    def imprimir_um_abaixo_do_outro(self):
        for i in range(1, 21):
            print(i)

    def imprimir_um_ao_lado_do_outro(self):
        numeros = ""
        for i in range(1, 21):
            numeros += str(i) + " "
        print(numeros)


def main():
    numeros = Numeros()
    numeros.imprimir_um_abaixo_do_outro()
    print()
    numeros.imprimir_um_ao_lado_do_outro()


if __name__ == "__main__":
    main()
