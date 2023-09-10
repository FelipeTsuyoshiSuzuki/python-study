results = [1, 1, 1, 2, 2]


def main():
    result = discover_number(int(input(), 10))
    print(result)


def discover_number(n):
    for i in range(1, n + 1):
        if i > len(results):
            list_item = results[4 + (i - 6)] + results[i - 6]
            results.append(list_item)
    return results[n - 1]


if __name__ == "__main__":
    main()
