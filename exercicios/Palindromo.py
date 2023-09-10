# verificar se algum caracter tem um número impar de ocorrencias
#   se sim: verificar se é o único
#       se não for o unico retornar falso | 0
#   se não houver caracter com numero impar: retornar verdadeiro | 1

def main():
    word = input()
    print(is_palindromo(word))


def is_palindromo(word):
    even = is_even(word)
    even_letter_count = get_even_letters_count(word)
    if even:
        if even_letter_count == 1:
            return 1
        else:
            return 0
    else:
        if even_letter_count == 0:
            return 1
        else:
            return 0


def get_even_letters_count(word):
    letters_count = letter_separator(word)
    even_letter_count = 0
    for i in letters_count:
        if letters_count[i] % 2 == 1:
            even_letter_count += 1
    return even_letter_count


def is_even(word, ):
    if len(word) % 2 == 1:
        return True
    else:
        return False


def letter_separator(word):
    word_occurence = {}
    for i in word.lower():
        if i not in word_occurence:
            word_occurence[i] = count_character(i, word)
    return word_occurence


def count_character(character, word):
    count = 0
    for i in word.lower():
        if i == character:
            count += 1
    return count


if __name__ == "__main__":
    main()
