#Lista de Exercício 5 - Questão 14
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

#8  3  4 
#1  5  9
#6  7  2
#Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

class QuadradoMagico:
    def __init__(self):
        self.resultados = []

    def encontra_quadrados_magicos(self):
        numeros = list(range(1, 10))
        self.permutacao_quadrados_magicos(numeros, [])

    def permutacao_quadrados_magicos(self, numeros, quadrado):
        if len(quadrado) == 9:
            if self.eh_quadrado_magico(quadrado):
                self.resultados.append(quadrado.copy())
        else:
            for num in numeros:
                if num not in quadrado:
                    quadrado.append(num)
                    self.permutacao_quadrados_magicos(numeros, quadrado)
                    quadrado.pop()

    def eh_quadrado_magico(self, quadrado):
        magica = sum(quadrado[:3])

        for i in range(3):
            if sum(quadrado[i::3]) != magica:  # verifica colunas
                return False

            if sum(quadrado[i * 3:(i * 3) + 3]) != magica:  # verifica linhas
                return False

        if sum(quadrado[::4]) != magica:  # verifica diagonal principal
            return False

        if sum(quadrado[2:8:2]) != magica:  # verifica diagonal secundária
            return False

        return True


try:
    quadrado_magico = QuadradoMagico()
    quadrado_magico.encontra_quadrados_magicos()

    print("Quadrados Mágicos encontrados:")
    for resultado in quadrado_magico.resultados:
        print(resultado[:3])
        print(resultado[3:6])
        print(resultado[6:9])
        print()

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
