#Lista de Exercício 3 - Questão 40
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
#Código da cidade;
#Número de veículos de passeio (em 1999);
#Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#Qual a média de veículos nas cinco cidades juntas;
#Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

class Cidade:
    def __init__(self, codigo, num_veiculos, num_acidentes):
        self.codigo = codigo
        self.num_veiculos = num_veiculos
        self.num_acidentes = num_acidentes


def calcular_estatisticas(cidades):
    if len(cidades) != 5:
        raise ValueError("É necessário fornecer dados de exatamente cinco cidades.")

    maior_indice = float("-inf")
    menor_indice = float("inf")
    cidade_maior_indice = None
    cidade_menor_indice = None
    soma_veiculos = 0
    soma_acidentes = 0
    count_cidades_menos_2000 = 0
    soma_acidentes_menos_2000 = 0

    for cidade in cidades:
        soma_veiculos += cidade.num_veiculos
        soma_acidentes += cidade.num_acidentes

        if cidade.num_veiculos < 2000:
            count_cidades_menos_2000 += 1
            soma_acidentes_menos_2000 += cidade.num_acidentes

        indice = cidade.num_acidentes / cidade.num_veiculos

        if indice > maior_indice:
            maior_indice = indice
            cidade_maior_indice = cidade

        if indice < menor_indice:
            menor_indice = indice
            cidade_menor_indice = cidade

    media_veiculos = soma_veiculos / len(cidades)
    media_acidentes_menos_2000 = soma_acidentes_menos_2000 / count_cidades_menos_2000

    return (
        cidade_maior_indice,
        cidade_menor_indice,
        media_veiculos,
        media_acidentes_menos_2000,
    )


def main():
    try:
        cidades = []
        for i in range(1, 6):
            codigo = int(input("Digite o código da cidade {}: ".format(i)))
            num_veiculos = int(input("Digite o número de veículos de passeio em 1999: "))
            num_acidentes = int(input("Digite o número de acidentes de trânsito com vítimas em 1999: "))

            cidade = Cidade(codigo, num_veiculos, num_acidentes)
            
            cidades.append(cidade)

        (
            cidade_maior_indice,
            cidade_menor_indice,
            media_veiculos,
            media_acidentes_menos_2000,
        ) = calcular_estatisticas(cidades)

        print("\nEstatísticas:")
        print("Maior índice de acidentes: {:.2f} - Cidade {}".format(
            cidade_maior_indice.num_acidentes / cidade_maior_indice.num_veiculos,
            cidade_maior_indice.codigo
        ))
        print("Menor índice de acidentes: {:.2f} - Cidade {}".format(
            cidade_menor_indice.num_acidentes / cidade_menor_indice.num_veiculos,
            cidade_menor_indice.codigo
        ))
        print("Média de veículos nas cinco cidades: {:.2f}".format(media_veiculos))
        print("Média de acidentes nas cidades com menos de 2000 veículos: {:.2f}".format(
            media_acidentes_menos_2000
        ))

    except ValueError as e:
        print("Erro: {}".format(e))

if __name__ == "__main__":
    main()
