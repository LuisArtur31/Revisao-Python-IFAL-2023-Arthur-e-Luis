#Lista de Exercício 1 - Questão 7
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

class Quadrado:
    def solicitar_lado(self):
        try:
            lado = float(input("Digite o valor do lado do quadrado: "))
            return lado
        except ValueError:
            print("Erro: Valor inválido. Por favor, digite um número válido.")
            return None

    def calcular_area(self, lado):
        try:
            area = lado ** 2
            return area
        except Exception as e:
            print("Erro ao calcular a área do quadrado:", e)
            return None

    def dobrar_area(self, area):
        try:
            area_dobrada = area * 2
            return area_dobrada
        except Exception as e:
            print("Erro ao dobrar a área do quadrado:", e)
            return None

def main():
    try:
        quadrado = Quadrado()
        lado = quadrado.solicitar_lado()

        if lado is not None:
            area = quadrado.calcular_area(lado)
            if area is not None:
                area_dobrada = quadrado.dobrar_area(area)
                if area_dobrada is not None:
                    print(f"A área do quadrado é {area} e o dobro dessa área é {area_dobrada}.")
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
