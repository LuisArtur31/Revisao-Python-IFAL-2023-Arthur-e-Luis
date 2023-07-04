#Lista de Exercício 3 - Questão 2
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

class Autenticacao:
    def autenticar_usuario(self):
        while True:
            usuario = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")

            if self.validar_senha(usuario, senha):
                print("Autenticação bem-sucedida.")
                break
            else:
                print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")

    def validar_senha(self, usuario, senha):
        return senha != usuario


def main():
    autenticacao = Autenticacao()
    autenticacao.autenticar_usuario()


if __name__ == "__main__":
    main()
