inf = float('inf')
def solution():                  
 
    n = int(input())
    weights = sorted(list(map(int, input().split())))
    ans = inf
    n*=2

    for ii in range(n):
        for jj in range(ii+1, n):
            B = []
            for k in range(n):
                if k!=ii and k!=jj:
                    B.append(weights[k])
            total = sum(B[i + 1] - B[i] for i in range(0, n - 2, 2))
            ans = min(ans, total)
    print(ans)
    
    # for ii in range(2*n - 2):
# 50
# 499 780 837 984 481 526 944 482 862 136 265 605 5 631 974 967 574 293 969 467 573 845 102 224 17 873 648 120 694 996 244 313 404 129 899 583 541 314 525 496 443 857 297 78 575 2 430 137 387 319 382 651 594 411 845 746 18 232 6 289 889 81 174 175 805 1000 799 950 475 713 951 685 729 925 262 447 139 217 788 514 658 572 784 185 112 636 10 251 621 218 210 89 597 553 430 532 264 11 160 476


if __name__ == "__main__":
    solution()