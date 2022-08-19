# import sys
# sys.stdin = open("rental.in","r")
# sys.stdout = open("rental.out","w")

def psum(l, n):
    p = [0]
    for i in range(n):
        p.append(p[-1])
        p[-1] += l[i]
    return p

def solution():
    n, m, r = map(int, input().split())
    milkVal = []
    milkSell = []
    cowBuy = []
    maxprofit = 0

    for ii in range(n): 
        milkVal.append(int(input()))
    for ii in range(m): 
        milkSell.append(list(map(int, input().split())))
    for ii in range(r): 
        cowBuy.append(int(input()))
    
    milkVal.sort(reverse=True)
    milkSell.sort(key=lambda x: x[1], reverse=True)
    cowBuy.sort(reverse=True)
    milkValp = psum(milkVal, n)
    cowBuyp = psum(cowBuy, r)

    for i in range(n): # change the range I think
        if i < m+1 and n-i < r+1:
            profit = 0
            # Sell the cows that product the least milk, starting with none
            profit += cowBuyp[i]
            # print("rented cows for", cowBuyp[i])
            # Sell the rest of their milk greedily
            milkAvail = milkValp[n-i]
            for offer in milkSell:
                
                # print("milk available - ", milkAvail)
                if offer[0] < milkAvail:
                    profit += offer[0] * offer[1]
                    milkAvail -= offer[0]
                    # print("sold", offer[0], "gals for", offer[1])
                else:
                    profit += offer[1] * milkAvail
                    milkAvail = 0 
                    # print("ran out of milk, sold", milkAvail, "for", offer[1])
                if milkAvail == 0:
                    break
            # print("profited - ", profit)
            maxprofit = max(maxprofit, profit)
    
    print(maxprofit)




if __name__ == "__main__":
    solution()