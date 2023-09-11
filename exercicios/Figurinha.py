# primeira entrada valor do pacote
# segunda entrada: moedas de 25, 10, 5, 1

def main():
    pack_value = input().lstrip("R$")
    quarter, ten, five, one = input().split(" ")
    coin_dict = {25: int(quarter), 10: int(ten), 5: int(five), 1: int(one)}
    pack = buy(float(pack_value), coin_dict)
    print(pack)
    print(sum(coin_dict.values()))


def buy(pack_value, coin_dict):
    money = get_total_money(coin_dict)
    packs = 0
    while money >= pack_value * 100:
        packs += 1
        value_to_pay = pack_value * 100
        while value_to_pay > 0:
            if coin_dict[25] > 0:
                value_to_pay -= 25
                money -= 25
                coin_dict[25] -= 1
            elif coin_dict[10] > 0:
                value_to_pay -= 10
                money -= 10
                coin_dict[10] -= 1
            elif coin_dict[5] > 0:
                value_to_pay -= 5
                money -= 5
                coin_dict[5] -= 1
            elif coin_dict[1] > 0:
                value_to_pay -= 1
                money -= 1
                coin_dict[1] -= 1
    return packs


def get_total_money(coin_dict):
    quarters = coin_dict[25] * 25
    ten = coin_dict[10] * 10
    five = coin_dict[5] * 5
    return quarters + ten + five + coin_dict[1]


if __name__ == "__main__":
    main()
