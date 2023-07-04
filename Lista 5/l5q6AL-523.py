#Lista de Exercício 5 - Questão 6
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

class HorarioConverter:
    def __init__(self, horas, minutos):
        self.horas = horas
        self.minutos = minutos

    def converter_horario(self):
        if self.horas > 12:
            self.horas -= 12
            self.periodo = 'P.M.'
        else:
            self.periodo = 'A.M.'

    def imprimir_horario(self):
        print(f"A conversão para o formato de 12 horas é: {self.horas}:{self.minutos:02d} {self.periodo}")

def main():
    try:
        while True:
            horas = int(input("Digite as horas (0-23): "))
            minutos = int(input("Digite os minutos (0-59): "))

            if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
                raise ValueError("Horário inválido. Certifique-se de digitar valores corretos.")

            converter = HorarioConverter(horas, minutos)
            converter.converter_horario()
            converter.imprimir_horario()

            opcao = input("Deseja converter outro horário? (s/n): ")
            if opcao.lower() != 's':
                break

    except ValueError as error:
        print(f"Erro: {str(error)}")

if __name__ == "__main__":
    main()
