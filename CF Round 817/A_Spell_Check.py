name_letters = ['T', 'i', 'u', 'm', 'r']
for _ in range(int(input())):
    n = int(input())
    s = input()

    if n != 5:
        print("NO")
    else:
        for letter in name_letters:
            if letter not in s:
                print("NO")
                break
        else:
            print("YES") 
