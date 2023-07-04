#Lista de Exercício 3 - Questão 33
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

class Temperaturas:
    def __init__(self):
        self.temperaturas = []

    def ler_temperaturas(self):
        while True:
            try:
                temperatura = float(input("Digite a temperatura (ou 0 para encerrar): "))
                if temperatura == 0:
                    break
                self.temperaturas.append(temperatura)
            except ValueError:
                print("Valor inválido. Digite uma temperatura válida.")

    def encontrar_menor(self):
        if not self.temperaturas:
            return None
        return min(self.temperaturas)

    def encontrar_maior(self):
        if not self.temperaturas:
            return None
        return max(self.temperaturas)

    def calcular_media(self):
        if not self.temperaturas:
            return None
        return sum(self.temperaturas) / len(self.temperaturas)


def main():
    conjunto_temperaturas = Temperaturas()
    conjunto_temperaturas.ler_temperaturas()

    menor = conjunto_temperaturas.encontrar_menor()
    maior = conjunto_temperaturas.encontrar_maior()
    media = conjunto_temperaturas.calcular_media()

    if menor is not None:
        print(f"Menor temperatura: {menor}")
    else:
        print("Nenhuma temperatura foi informada.")

    if maior is not None:
        print(f"Maior temperatura: {maior}")
    else:
        print("Nenhuma temperatura foi informada.")

    if media is not None:
        print(f"Média das temperaturas: {media}")
    else:
        print("Nenhuma temperatura foi informada.")


if __name__ == "__main__":
    main()
