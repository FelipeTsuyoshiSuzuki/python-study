def main():
    gas_value = float(input())
    etanol_value = float(input())
    print(is_better(gas_value, etanol_value))


def  is_better(gas_value, etanol_value):
    if etanol_value / gas_value < 0.7:
        return "ETANOL"
    else:
        return "GASOLINA"


if __name__ == "__main__":
    main()