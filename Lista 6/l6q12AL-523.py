#Lista de Exercício 6 - Questão 12
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

#Valida e corrige número de telefone
#Telefone: 461-0133
#Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
#Telefone corrigido sem formatação: 34610133
#Telefone corrigido com formatação: 3461-0133

class CorretorTelefone:
    def __init__(self, telefone):
        self.telefone = telefone

    def _remover_caracteres_formatacao(self, telefone):
        # Remove os caracteres de formatação do telefone
        telefone_formatado = telefone.replace("-", "")
        return telefone_formatado

    def corrigir_telefone(self):
        try:
            telefone_formatado = self._remover_caracteres_formatacao(self.telefone)

            if len(telefone_formatado) == 7:
                telefone_corrigido = "3" + telefone_formatado
                telefone_corrigido_formatado = telefone_corrigido[:4] + "-" + telefone_corrigido[4:]
                return telefone_corrigido, telefone_corrigido_formatado
            elif len(telefone_formatado) == 8:
                telefone_corrigido = telefone_formatado
                telefone_corrigido_formatado = telefone_corrigido[:4] + "-" + telefone_corrigido[4:]
                return telefone_corrigido, telefone_corrigido_formatado
            else:
                return None, None

        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')
            return None, None


def main():
    try:
        telefone = input("Digite o número de telefone: ")

        corretor = CorretorTelefone(telefone)
        telefone_corrigido, telefone_corrigido_formatado = corretor.corrigir_telefone()

        if telefone_corrigido is not None:
            print(f"Telefone possui {len(telefone)} dígitos. Vou acrescentar o dígito três na frente.")
            print(f"Telefone corrigido sem formatação: {telefone_corrigido}")
            print(f"Telefone corrigido com formatação: {telefone_corrigido_formatado}")
        else:
            print("Número de telefone inválido.")

    except Exception as e:
        print(f'Ocorreu um erro: {str(e)}')


if __name__ == '__main__':
    main()
