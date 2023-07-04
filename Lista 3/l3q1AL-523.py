#Lista de Exercício 3 - Questão 1
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

class VerificadorNota:
    def verificar_nota(self):
        while True:
            try:
                nota = float(input("Digite uma nota entre zero e dez: "))
                if 0 <= nota <= 10:
                    return nota
                else:
                    print("Valor inválido. A nota deve estar entre zero e dez.")
            except ValueError:
                print("Valor inválido. Certifique-se de digitar um número.")

try:
    verificador = VerificadorNota()

    nota = verificador.verificar_nota()

    print(f"Nota válida: {nota}")
except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
