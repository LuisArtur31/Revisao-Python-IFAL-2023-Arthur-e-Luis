#Lista de Exercício 7 - Questão 1
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Bola: Crie uma classe que modele uma bola:

#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor


try:
    # Exemplo de uso da classe Bola
    minha_bola = Bola("vermelha", 10, "couro")

    print("Cor da bola:", minha_bola.mostraCor())

    nova_cor = input("Digite a nova cor da bola: ")
    minha_bola.trocaCor(nova_cor)

    print("Cor da bola atualizada:", minha_bola.mostraCor())

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
