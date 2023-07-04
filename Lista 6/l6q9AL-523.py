#Lista de Exercício 6 - Questão 9
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

class ValidadorCPF:
    def __init__(self, cpf):
        self.cpf = cpf

    def _remover_caracteres_formato(self, cpf):
        # Remove os caracteres de formatação do CPF
        cpf_formatado = cpf.replace(".", "").replace("-", "")
        return cpf_formatado

    def _validar_digitos_verificadores(self, cpf_formatado):
        # Verifica se os dígitos verificadores do CPF são válidos
        cpf_base = cpf_formatado[:9]
        digitos_verificadores = cpf_formatado[9:]

        soma = 0
        for i, digito in enumerate(cpf_base):
            soma += int(digito) * (10 - i)

        primeiro_digito = (soma * 10) % 11
        if primeiro_digito == 10:
            primeiro_digito = 0

        if int(digitos_verificadores[0]) != primeiro_digito:
            return False

        soma = 0
        for i, digito in enumerate(cpf_base + str(primeiro_digito)):
            soma += int(digito) * (11 - i)

        segundo_digito = (soma * 10) % 11
        if segundo_digito == 10:
            segundo_digito = 0

        if int(digitos_verificadores[1]) != segundo_digito:
            return False

        return True

    def verificar_cpf(self):
        try:
            cpf_formatado = self._remover_caracteres_formato(self.cpf)

            if len(cpf_formatado) != 11 or not cpf_formatado.isdigit():
                return False

            if not self._validar_digitos_verificadores(cpf_formatado):
                return False

            return True

        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')
            return False


def main():
    try:
        cpf = input('Digite um número de CPF (xxx.xxx.xxx-xx): ')

        validador = ValidadorCPF(cpf)
        if validador.verificar_cpf():
            print('CPF válido.')
        else:
            print('CPF inválido.')

    except Exception as e:
        print(f'Ocorreu um erro: {str(e)}')


if __name__ == '__main__':
    main()
