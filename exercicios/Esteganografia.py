# A = 0
# B = 1
# UTILIZAR BINARIO EM VEZ DA TABELA BACON
def main():
    bacon_text = fake_to_bacon(input())
    print(bacon_text)
    print(bacon_to_text(bacon_text))


def fake_to_bacon(text):
    baconString = []
    for i in text:
        if 65 <= ord(i) <= 90:
            baconString.append("B")
        elif 97 <= ord(i) <= 122:
            baconString.append("A")
    return baconString


def bacon_to_text(baconText):
    final_string = ""
    separator = []
    for i in baconText:
        if len(separator) == 8:
            bin_string = convert_bacon_to_bin(separator)
            character = convert_bin_to_char(bin_string)
            if character != None:
                final_string += character
            separator.clear()

        separator.append(i)
    return final_string.rstrip('\x00')


def convert_bacon_to_bin(bacon_string):
    bin_string = ""
    for i in bacon_string:
        if i == 'A':
            bin_string += '0'
        elif i == 'B':
            bin_string += '1'
        else:
            return None
    return bin_string


def convert_bin_to_char(bin_string):
    global bin
    if bin_string != None:
        bin = int(bin_string, 2)
    else:
        return None
    return chr(bin)


if __name__ == "__main__":
    main()
