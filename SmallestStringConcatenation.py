from functools import cmp_to_key

def solution():
    n = int(input())
    A = []
    for i in range(n): 
        A.append(input())
    sA = sorted(A, key=cmp_to_key(lambda a,b: a+b>b+a))
    for w in sA:
        print(w, end = '')
    print()


if __name__ == "__main__":
    solution()