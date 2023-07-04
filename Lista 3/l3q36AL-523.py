#Lista de Exercício 3 - Questão 36
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
#Montar a tabuada de: 5
#Começar por: 4
#Terminar em: 7

#Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#5 X 4 = 20
#5 X 5 = 25
#5 X 6 = 30
#5 X 7 = 35
#Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

class T:
    def gerar_t(self):
        try:
            numero = int(input("Montar a tabuada de: "))
            inicio = int(input("Começar por: "))
            fim = int(input("Terminar em: "))

            if fim < inicio:
                raise ValueError("O valor final não pode ser menor que o valor inicial.")

        except ValueError as e:
            print(f"Entrada inválida: {e}")
            return

        print(f"\nVou montar a tabuada de {numero} começando em {inicio} e terminando em {fim}:")
        for i in range(inicio, fim + 1):
            resultado = numero * i
            print(f"{numero} X {i} = {resultado}")


def main():
    tabuada = T()
    tabuada.gerar_t()


if __name__ == "__main__":
    main()
