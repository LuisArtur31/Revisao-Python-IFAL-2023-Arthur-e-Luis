#Lista de Exercício 6 - Questão 14
#Dupla: 2021314680 - Arthur Durval Santos Silva Caetano e 2021314948 - Luís Artur Holanda Santos
#Disciplina: Programação Web
#Professor: Italo Arruda

#Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.

class LeetTranslator:
    def __init__(self):
        self.mapping = {
            'a': '4',
            'e': '3',
            'i': '1',
            'o': '0',
            's': '5',
            't': '7',
            'b': '8',
        }

    def translate(self, text):
        translated_text = ''
        for char in text:
            translated_text += self.mapping.get(char.lower(), char)
        return translated_text

def main():
    translator = LeetTranslator()
    text = input("Digite o texto: ")
    leet_text = translator.translate(text)
    print("Texto em Leet Speak:", leet_text)

if __name__ == '__main__':
    main()
