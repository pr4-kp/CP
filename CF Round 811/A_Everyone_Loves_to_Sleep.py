inf = float('inf')
def solution():
    for _ in range(int(input())):
        n, h, m = map(int, input().split())
        ansH = ansM = 0
        curmin = inf

        for ii in range(n): 
            alarmH, alarmM = map(int, input().split())
            # compare to in 24 hour period and after period
            if alarmH == alarmM:
                ansH = ansM = 0
            t = (alarmH - h) * 60 + alarmM - m
            if (alarmH - h) * 60 + alarmM - m < 0:
                t = (alarmH - h + 24) * 60 + alarmM - m

            curmin = min(curmin, t)

        print(curmin // 60, curmin % 60)

            
                    




if __name__ == "__main__":
    solution()