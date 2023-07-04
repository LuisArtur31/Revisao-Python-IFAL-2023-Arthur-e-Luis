#Lista de Exercício 1 - Questão 11
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

class Pessoa:
    def __init__(self, altura, sexo):
        self.altura = altura
        self.sexo = sexo

    def calcular_peso_ideal(self):
        if self.sexo == "M":
            peso_ideal = (62.1 * self.altura) - 44.7
        elif self.sexo == "H":
            peso_ideal = (72.7 * self.altura) - 58
        else:
            raise ValueError("Sexo inválido. Use 'M' para mulheres e 'H' para homens.")
        return peso_ideal


def ler_altura():
    try:
        altura = float(input("Digite a altura (em metros): "))
        return altura
    except ValueError:
        print("Erro: Digite uma altura válida.")
        return ler_altura()


def ler_sexo():
    sexo = input("Digite o sexo (M para mulheres, H para homens): ").upper()
    if sexo not in ["M", "H"]:
        print("Erro: Sexo inválido. Use 'M' para mulheres e 'H' para homens.")
        return ler_sexo()
    return sexo


try:
    altura = ler_altura()
    sexo = ler_sexo()

    pessoa = Pessoa(altura, sexo)
    peso_ideal = pessoa.calcular_peso_ideal()

    print(f"O peso ideal é: {peso_ideal:.2f} kg")

except ValueError as error:
    print(f"Erro: {str(error)}")
