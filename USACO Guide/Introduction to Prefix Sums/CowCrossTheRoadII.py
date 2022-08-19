import sys
sys.stdin = open("maxcross.in","r")
sys.stdout = open("maxcross.out","w")

def solution():
    n, k, b = map(int, input().split())
    lights = [0] * n
    psumLights = [0]
    diff = []

    for i in range(b):
        ID = int(input()) - 1
        lights[ID] = 1
    for i in range(n):
        psumLights.append(psumLights[-1])
        psumLights[-1] += lights[i]

    for i in range(n-k+1):
        diff.append(psumLights[i+k] - psumLights[i])
    print(min(diff))



if __name__ == "__main__":
    solution()