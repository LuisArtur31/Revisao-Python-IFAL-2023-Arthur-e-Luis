#Lista de Exercício 4 - Questão 23
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
#alexandre       456123789
#anderson        1245698456
#antonio         123456456
#carlos          91257581
#cesar           987458
#rosemary        789456125
#Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
#ACME Inc.               Uso do espaço em disco pelos usuários
#------------------------------------------------------------------------
#Nr.  Usuário        Espaço utilizado     % do uso

#1    alexandre       434,99 MB             16,85%
#2    anderson       1187,99 MB             46,02%
#3    antonio         117,73 MB              4,56%
#4    carlos           87,03 MB              3,37%
#5    cesar             0,94 MB              0,04%
#6    rosemary        752,88 MB             29,16%

#Espaço total ocupado: 2581,57 MB
#Espaço médio ocupado: 430,26 MB
#O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

class Usuario:
    def __init__(self, nome, espaco):
        self.nome = nome
        self.espaco = espaco

    def calcular_porcentagem(self, total):
        return (self.espaco / total) * 100

    def calcular_espaco_mb(self):
        return self.espaco / (1024 * 1024)

    def formatar_espaco(self):
        espaco_mb = self.calcular_espaco_mb()
        return f"{espaco_mb:.2f} MB"


def ler_arquivo_usuarios():
    usuarios = []

    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    nome, espaco = linha.split()
                    usuarios.append(Usuario(nome, int(espaco)))
    except FileNotFoundError:
        print("Arquivo 'usuarios.txt' não encontrado.")
    except ValueError:
        print("Erro ao ler os dados dos usuários no arquivo.")

    return usuarios


def gerar_relatorio(usuarios):
    total_espaco = sum(usuario.espaco for usuario in usuarios)
    espaco_medio = total_espaco / len(usuarios)

    relatorio = []
    relatorio.append("ACME Inc.               Uso do espaço em disco pelos usuários")
    relatorio.append("-" * 70)
    relatorio.append("Nr.  Usuário        Espaço utilizado     % do uso")
    relatorio.append("")

    for i, usuario in enumerate(usuarios, 1):
        porcentagem = usuario.calcular_porcentagem(total_espaco)
        relatorio.append(f"{i:<4}  {usuario.nome:<15}  {usuario.formatar_espaco():<15}  {porcentagem:.2f}%")

    relatorio.append("")
    relatorio.append(f"Espaço total ocupado: {usuario.formatar_espaco()} MB")
    relatorio.append(f"Espaço médio ocupado: {espaco_medio / (1024 * 1024):.2f} MB")

    return relatorio


def salvar_relatorio(relatorio):
    try:
        with open("relatorio.txt", "w") as arquivo:
            arquivo.write("\n".join(relatorio))
    except IOError:
        print("Erro ao salvar o relatório.")


def main():
    usuarios = ler_arquivo_usuarios()

    if usuarios:
        relatorio = gerar_relatorio(usuarios)
        salvar_relatorio(relatorio)
        print("Relatório gerado com sucesso no arquivo 'relatorio.txt'.")


if __name__ == "__main__":
    main()
