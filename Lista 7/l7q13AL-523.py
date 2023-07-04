#Lista de Exercício 7 - Questão 13
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario


# Exemplo de uso:
funcionario = Funcionario("João", 2500.0)
print("Nome do funcionário:", funcionario.getNome())
print("Salário do funcionário:", funcionario.getSalario())
