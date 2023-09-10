def main():
    n = input()
    numbers_dict = separate_numbers(n)
    is_divisible_by_3(numbers_dict['even'])
    is_divisible_by_3(numbers_dict['odd'])


def is_divisible_by_3(number_list):
    if sum(number_list) % 3 == 0:
        print('S')
    else:
        print('N')


def separate_numbers(n):
    n_dict = {'odd': [], 'even': []}
    for i in n:
        if int(i) % 2 == 0:
            n_dict['even'].append(int(i))
        else:
            n_dict['odd'].append(int(i))
    return n_dict


if __name__ == "__main__":
    main()
