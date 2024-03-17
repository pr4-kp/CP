f = open("input.txt", "r")

cur = 0
sizes = []

with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        if line.strip():
            cur += int(line.strip())
        else:
            sizes.append(cur)
            cur = 0

sizes.sort()

print(sizes[-1] + sizes[-2] + sizes[-3])
