#Lista de Exercício 4 - Questão 13
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

class TemperaturaAnual:
    def __init__(self):
        self.temperaturas = []

    def ler_temperaturas(self):
        for mes in range(1, 13):
            while True:
                try:
                    temperatura = float(input(f"Digite a temperatura média do mês {mes}: "))
                    self.temperaturas.append(temperatura)
                    break
                except ValueError:
                    print("Valor inválido. Digite um número.")

    def calcular_media_anual(self):
        media = sum(self.temperaturas) / len(self.temperaturas)
        return media

    def mostrar_temperaturas_acima_media(self, media):
        print("Temperaturas acima da média anual:")
        for mes, temperatura in enumerate(self.temperaturas, start=1):
            if temperatura > media:
                nome_mes = self.obter_nome_mes(mes)
                print(f"{nome_mes}: {temperatura} °C")

    @staticmethod
    def obter_nome_mes(numero_mes):
        meses = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
        return meses[numero_mes - 1]


def main():
    temperatura_anual = TemperaturaAnual()
    temperatura_anual.ler_temperaturas()
    media = temperatura_anual.calcular_media_anual()
    temperatura_anual.mostrar_temperaturas_acima_media(media)


if __name__ == "__main__":
    main()
