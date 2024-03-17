points = 0

with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        enemy, you = line.split()
        if you == "Z":
            if enemy == "A":
                points += 8
            elif enemy == "B":
                points += 9
            else:
                points += 7
        elif you == "Y":
            if enemy == "A":
                points += 4
            elif enemy == "B":
                points += 5
            else:
                points += 6
        else:
            if enemy == "A":
                points += 3
            elif enemy == "B":
                points += 1 
            else:
                points += 2

print(points)