#Lista de Exercício 2 - Questão 3
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

class VerificadorSexo:
    def __init__(self):
        self.letra = None

    def solicitar_letra(self):
        while True:
            try:
                self.letra = input("Digite uma letra (F ou M): ").upper()
                if self.letra not in ["F", "M"]:
                    raise ValueError
                break
            except ValueError:
                print("Sexo Inválido! Digite apenas a letra F para Feminino ou M para Masculino!")

    def verificar_sexo(self):
        if self.letra == "F":
            return "Feminino"
        elif self.letra == "M":
            return "Masculino"
        else:
            return "Sexo Inválido"


try:
    verificador = VerificadorSexo()
    verificador.solicitar_letra()
    resultado = verificador.verificar_sexo()

    print("Resultado:", resultado)

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
