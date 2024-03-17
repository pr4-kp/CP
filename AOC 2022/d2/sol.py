points = 0

with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        enemy, you = line.split()
        if you == "X":
            points += 1
            if enemy == "A":
                points += 3
            elif enemy == "B":
                points += 0 
            else:
                points += 6
        elif you == "Y":
            points += 2
            if enemy == "A":
                points += 6
            elif enemy == "B":
                points += 3 
            else:
                points += 0
        else:
            points += 3
            if enemy == "A":
                points += 0
            elif enemy == "B":
                points += 6 
            else:
                points += 3

print(points)