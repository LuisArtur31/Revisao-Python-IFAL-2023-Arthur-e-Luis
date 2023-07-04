#Lista de Exercício 3 - Questão 3
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

class ValidadorInformacoes:
    def validar_nome(self, nome):
        if len(nome) > 3:
            return True
        else:
            return False

    def validar_idade(self, idade):
        if 0 <= idade <= 150:
            return True
        else:
            return False

    def validar_salario(self, salario):
        if salario > 0:
            return True
        else:
            return False

    def validar_sexo(self, sexo):
        if sexo == 'f' or sexo == 'm':
            return True
        else:
            return False

    def validar_estado_civil(self, estado_civil):
        if estado_civil in ['s', 'c', 'v', 'd']:
            return True
        else:
            return False


try:
    validador = ValidadorInformacoes()

    nome = input("Digite o nome: ")
    while not validador.validar_nome(nome):
        print("Nome inválido. Deve conter mais de 3 caracteres.")
        nome = input("Digite o nome: ")

    idade = int(input("Digite a idade: "))
    while not validador.validar_idade(idade):
        print("Idade inválida. Deve estar entre 0 e 150.")
        idade = int(input("Digite a idade: "))

    salario = float(input("Digite o salário: "))
    while not validador.validar_salario(salario):
        print("Salário inválido. Deve ser maior que zero.")
        salario = float(input("Digite o salário: "))

    sexo = input("Digite o sexo (f/m): ")
    while not validador.validar_sexo(sexo):
        print("Sexo inválido. Deve ser 'f' ou 'm'.")
        sexo = input("Digite o sexo (f/m): ")

    estado_civil = input("Digite o estado civil (s/c/v/d): ")
    while not validador.validar_estado_civil(estado_civil):
        print("Estado civil inválido. Deve ser 's', 'c', 'v' ou 'd'.")
        estado_civil = input("Digite o estado civil (s/c/v/d): ")

    print("Informações válidas. Cadastro concluído.")
except ValueError as error:
    print("Valor inválido. Certifique-se de digitar um valor numérico quando solicitado.")
except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
