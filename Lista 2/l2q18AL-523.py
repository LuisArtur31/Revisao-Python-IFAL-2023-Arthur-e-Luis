#Lista de Exercício 2 - Questão 18
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

class DataInvalidaException(Exception):
    pass


class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def verificar_data(self):
        # Verificar se o ano é bissexto
        if self.ano % 4 == 0 and (self.ano % 100 != 0 or self.ano % 400 == 0):
            dias_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Verificar se o mês e o dia estão dentro dos limites
        if self.mes < 1 or self.mes > 12 or self.dia < 1 or self.dia > dias_mes[self.mes - 1]:
            raise DataInvalidaException("Data inválida.")

    def imprimir_data(self):
        print(f"A data {self.dia}/{self.mes}/{self.ano} é válida.")


def main():
    try:
        data_str = input("Digite uma data no formato dd/mm/aaaa: ")
        dia, mes, ano = map(int, data_str.split("/"))
        data = Data(dia, mes, ano)
        data.verificar_data()
        data.imprimir_data()
    except (ValueError, DataInvalidaException) as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
