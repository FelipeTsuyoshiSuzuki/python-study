# muda para o primeiro set 11011 = 27
# muda para o segundo set 11111 = 31

def main():
    first_set = create_set(input())
    second_set = create_set(input())
    encrypt_string = input()
    encrypt_set = (create_encrypt_set(encrypt_string))
    print(decrypt(first_set, second_set, encrypt_set))


def decrypt(set1, set2, encrypt_set):
    using_set = set1
    result = ""
    for i in encrypt_set:
        value = int(i, 2)
        if value == 31:
            using_set = set2
        elif value == 27:
            using_set == set1
        else:
            result += using_set[value]
    return result


def create_encrypt_set(encrypt_string):
    set = ""
    list_set = []
    for i in encrypt_string:
        set += i
        if len(set) == 5:
            list_set.append(set)
            set = ""
    return list_set


def create_set(char_list):
    set = []
    for i in char_list:
        set.append(i)
    return set


if __name__ == "__main__":
    main()