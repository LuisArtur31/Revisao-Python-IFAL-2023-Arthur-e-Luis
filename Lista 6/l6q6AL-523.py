#Lista de Exercício 6 - Questão 6
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

#Data de Nascimento: 29/10/1973
#Você nasceu em  29 de Outubro de 1973.

class DtNasc:
    def __init__(self, data):
        self.data = data

    def obter_mes_extenso(self, mes):
        meses = {
            1: 'Janeiro',
            2: 'Fevereiro',
            3: 'Março',
            4: 'Abril',
            5: 'Maio',
            6: 'Junho',
            7: 'Julho',
            8: 'Agosto',
            9: 'Setembro',
            10: 'Outubro',
            11: 'Novembro',
            12: 'Dezembro'
        }
        return meses.get(mes, 'Mês inválido')

    def imprimir_data_por_extenso(self):
        try:
            dia, mes, ano = map(int, self.data.split('/'))
            mes_extenso = self.obter_mes_extenso(mes)
            print(f'Você nasceu em {dia} de {mes_extenso} de {ano}.')
        except ValueError:
            print('Data inválida. Certifique-se de digitar no formato dd/mm/aaaa.')

def main():
    try:
        data = input('Digite sua data de nascimento (dd/mm/aaaa): ')

        data_nascimento = DtNasc(data)
        data_nascimento.imprimir_data_por_extenso()

    except Exception as e:
        print(f'Ocorreu um erro: {str(e)}')

if __name__ == '__main__':
    main()
