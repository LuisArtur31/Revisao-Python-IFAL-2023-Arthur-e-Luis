#Lista de Exercício 5 - Questão 13
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

class MolduraRetangulo:
    def __init__(self, linhas=1, colunas=1):
        self.linhas = max(1, min(linhas, 20))
        self.colunas = max(1, min(colunas, 20))

    def desenha_moldura(self):
        print('+' + '-' * (self.colunas - 2) + '+')

        for _ in range(self.linhas - 2):
            print('|' + ' ' * (self.colunas - 2) + '|')

        if self.linhas > 1:
            print('+' + '-' * (self.colunas - 2) + '+')

try:
    linhas = int(input("Digite o número de linhas (1 a 20): "))
    colunas = int(input("Digite o número de colunas (1 a 20): "))

    moldura = MolduraRetangulo(linhas, colunas)
    moldura.desenha_moldura()

except ValueError:
    print("Valor inválido. Certifique-se de digitar um número inteiro.")
except Exception as e:
    print("Ocorreu um erro:", str(e))
