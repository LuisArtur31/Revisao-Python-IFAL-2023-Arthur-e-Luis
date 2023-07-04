#Lista de Exercício 1 - Questão 5
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que converta metros para centímetros.

class Conversor:
    def solicitar_metros(self):
        try:
            metros = float(input("Digite a quantidade de metros: "))
            return metros
        except ValueError:
            print("Erro: Valor inválido. Por favor, digite um número válido.")
            return None

    def converter_para_centimetros(self, metros):
        try:
            centimetros = metros * 100
            return centimetros
        except Exception as e:
            print("Erro ao converter para centímetros:", e)
            return None

def main():
    try:
        conversor = Conversor()
        metros = conversor.solicitar_metros()

        if metros is not None:
            centimetros = conversor.converter_para_centimetros(metros)
            if centimetros is not None:
                print(f"{metros} metros equivalem a {centimetros} centímetros.")
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
