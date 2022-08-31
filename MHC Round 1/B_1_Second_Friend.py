import sys
sys.stdin = open("second_friend_input.txt", "r")
sys.stdout = open("second_friend_output.txt", "w")
inf = float('inf')
def arr_in():
    return list(map(int, input().split()))

def tup_in():
    return map(int, input().split())

def solution():
    for t in range(1, int(input()) + 1):
        result = "Case #" + str(t) + ": "
        map = []
        r, c = tup_in()
        for _ in range(r):
            map.append(input())
        if r == 1 or c == 1:
            for row in map:
                if '^' in row:
                    result += "Impossible"
                    print(result)
                    break 
            else:
                result += "Possible"
                print(result)
                for row in map:
                    print(row)
        else:
            result += "Possible"
            print(result)
            for _ in range(r):
                print('^' * c)

if __name__ == "__main__":
    solution()