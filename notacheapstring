class Choice:
    def __init__(self, cost, index):
        self.cost = cost 
        self.index = index

def solution():
    for _ in range(int(input())):
        numList = [ord(char) - 96 for char in input().lower()]
        wordlen = len(numList)
        wordList = [chr(char+96) for char in numList]
        goalreduction = int(input()) - sum(numList)
        
        choices = [Choice(numList[i], i) for i in range(wordlen)]
        
        choices.sort(key=lambda x: int(x.cost), reverse = True)
        rem = [0] * wordlen

        for ii in range(wordlen):
            if (goalreduction < 0):
                goalreduction += choices[ii].cost
                rem[choices[ii].index] = 1
        for ii in range(wordlen):
            if not rem[ii]:
                print(wordList[ii], end='')
        print()

if __name__ == "__main__":
    solution()
