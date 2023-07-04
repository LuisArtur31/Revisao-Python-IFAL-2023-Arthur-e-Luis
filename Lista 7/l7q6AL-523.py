#Lista de Exercício 7 - Questão 6
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class TV:
    def __init__(self):
        self.__canal = 1  # Atributo privado para encapsulamento
        self.__volume = 50

    def alterar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.__canal = novo_canal
        else:
            raise ValueError("O número do canal deve estar entre 1 e 100.")

    def aumentar_volume(self):
        if self.__volume < 100:
            self.__volume += 1

    def diminuir_volume(self):
        if self.__volume > 0:
            self.__volume -= 1

    def retornar_status(self):
        return f"Canal: {self.__canal}, Volume: {self.__volume}"


# Exemplo de uso:
tv = TV()
print("Status inicial:", tv.retornar_status())

try:
    while True:
        try:
            novo_canal = int(input("Digite o número do canal desejado: "))
            tv.alterar_canal(novo_canal)
            break
        except ValueError:
            print("Valor inválido! Digite um número válido.")

    print("Status após alterar o canal:", tv.retornar_status())

    while True:
        opcao = input("Deseja aumentar (A) ou diminuir (D) o volume? ")
        if opcao.upper() == "A":
            tv.aumentar_volume()
            break
        elif opcao.upper() == "D":
            tv.diminuir_volume()
            break
        else:
            print("Opção inválida! Digite 'A' para aumentar ou 'D' para diminuir.")

    print("Status após ajustar o volume:", tv.retornar_status())

except ValueError as e:
    print("Erro:", str(e))
