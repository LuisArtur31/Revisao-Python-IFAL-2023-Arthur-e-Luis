#Lista de Exercício 1 - Questão 1
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que mostre a mensagem "Alô mundo" na tela.

class Mensagem:
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def mostrar_mensagem(self):
        try:
            print(self.mensagem)
        except Exception as e:
            print("Erro ao exibir mensagem:", e)

def main():
    try:
        mensagem = Mensagem("Alô mundo")
        mensagem.mostrar_mensagem()
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
