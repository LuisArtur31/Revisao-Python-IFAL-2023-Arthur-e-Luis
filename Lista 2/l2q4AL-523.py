#Lista de Exercício 2 - Questão 4
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

class ValorInvalidoException(Exception):
    pass


class VerificadorLetra:
    def __init__(self):
        self.letra = None

    def ler_letra(self):
        while True:
            try:
                self.letra = input("Digite uma letra: ")
                if not self.letra.isalpha():
                    raise ValorInvalidoException("Valor inválido. Digite apenas uma letra.")
                break
            except ValorInvalidoException as e:
                print(f"Erro: {str(e)}")

    def verificar_vogal_consoante(self):
        if self.letra is None:
            raise ValorInvalidoException("Nenhuma letra foi informada.")

        vogais = ['a', 'e', 'i', 'o', 'u']
        if self.letra.lower() in vogais:
            return "A letra é uma vogal."
        else:
            return "A letra é uma consoante."


def main():
    verificador = VerificadorLetra()

    try:
        verificador.ler_letra()
        resultado = verificador.verificar_vogal_consoante()
        print(resultado)
    except ValorInvalidoException as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
