def main():
    qnt_habitantes = int(input())
    qnt_vacinados = int(input())
    percentage = qnt_vacinados / qnt_habitantes
    percentage = round(percentage * 100, 1)
    print(f"{percentage}%")


if __name__ == "__main__":
    main()