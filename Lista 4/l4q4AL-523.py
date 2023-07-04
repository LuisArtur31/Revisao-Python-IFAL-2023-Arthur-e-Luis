#Lista de Exercício 4 - Questão 4
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

class Vetor:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.caracteres = []

    def ler_caracteres(self):
        for i in range(self.tamanho):
            while True:
                try:
                    caractere = input(f"Digite o caractere {i+1}: ")
                    if len(caractere) != 1:
                        raise ValueError
                    break
                except ValueError:
                    print("Valor inválido. Digite um único caractere.")
            self.caracteres.append(caractere)

    def contar_consoantes(self):
        consoantes = []
        for caractere in self.caracteres:
            if caractere.lower() not in 'aeiou':
                consoantes.append(caractere)
        return len(consoantes), consoantes


def main():
    vetor = Vetor(10)
    vetor.ler_caracteres()
    qtd_consoantes, consoantes = vetor.contar_consoantes()

    print(f"Quantidade de consoantes: {qtd_consoantes}")
    print("Consoantes lidas:")
    for consoante in consoantes:
        print(consoante)


# Execução do programa
if __name__ == '__main__':
    main()
