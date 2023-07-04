#Lista de Exercício 5 - Questão 12
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

import random

class Embaralhador:
    def __init__(self, palavra):
        self.palavra = palavra

    def embaralhar(self):
        palavra_embaralhada = ''.join(random.sample(self.palavra.upper(), len(self.palavra)))
        return palavra_embaralhada


def main():
    while True:
        try:
            palavra = input("Digite uma palavra: ")
            em = Embaralhador(palavra)
            palavra_embaralhada = em.embaralhar()
            print(f"Palavra embaralhada: {palavra_embaralhada}")
        except Exception as e:
            print(f"Erro: {str(e)}")

        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            break


if __name__ == "__main__":
    main()
