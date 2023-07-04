#Lista de Exercício 5 - Questão 11
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

class Data:
    def __init__(self, data):
        self.data = data

    def validar_data(self):
        dia, mes, ano = map(int, self.data.split('/'))
        
        # Verifica se a data é válida
        if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1:
            return False

        # Verifica se o dia é válido para o mês
        if dia > 28:
            if mes == 2:
                if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                    if dia > 29:
                        return False
                else:
                    if dia > 28:
                        return False
            elif mes in [4, 6, 9, 11] and dia > 30:
                return False

        return True

    def converter_data(self):
        if self.validar_data():
            dia, mes, ano = map(int, self.data.split('/'))

            meses = [
                'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
                'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
            ]

            data_formatada = f'{dia} de {meses[mes-1]} de {ano}'

            return data_formatada
        else:
            return None


def main():
    while True:
        try:
            data_input = input("Digite uma data (DD/MM/AAAA): ")
            data_obj = Data(data_input)
            data_formatada = data_obj.converter_data()

            if data_formatada:
                print(f'Data formatada: {data_formatada}')
            else:
                print('Data inválida. Digite uma data válida.')

        except ValueError:
            print("Erro: formato de data inválido. Digite uma data no formato correto.")

        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            break


if __name__ == "__main__":
    main()
