# se for par n / 2
# se for impar (n * 3) + 1

def main():
    n = input()
    print(syracuse(int(n)))

def syracuse(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (n * 3) + 1
        count += 1
    return count


if __name__ == "__main__":
    main()