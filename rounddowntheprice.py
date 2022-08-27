def solution():
    for _ in range(int(input())):
        price = input()
        roundedprice = 10**(len(price)-1)
        print(int(price)-roundedprice)


if __name__ == "__main__":
    solution()