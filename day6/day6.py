INPUT_FILE = "input"

# PART 1
problems = []
rows = []

with open(INPUT_FILE, "r") as f:
    for row in f:
        row = row
        if len(problems) == 0:
            problems = [[x] for x in row.split(" ") if len(x) > 0]
            rows = [[x] for x in row]
        else:
            i = 0
            for x in row.split(" "):
                if x == "\n":
                    continue
                if len(x) == 0:
                    continue
                problems[i].append(x)
                i += 1
            for i,x in enumerate(row):
                rows[i].append(x)

total = 0

for prob in problems:
    if prob[-1] == "+":
        for x in prob[:-1]:
            total += int(x)
    elif prob[-1] == "*":
        acc = 1
        for x in prob[:-1]:
            acc *= int(x)
        total += acc

print(f"total (part 1): {total}")


# PART 2
symbol = ""
total = 0
acc = 0
for row in rows[:-1]:
    if row[-1] in ["*", "+"]:
        total += acc
        symbol = row[-1]
        if symbol == "+":
            acc = 0
        else:
            acc = 1
    row_s = "".join(row[:-1]).strip()
    if len(row_s) == 0:
        continue
    n = int(row_s)
    if symbol == "*":
        acc *= n
    elif symbol == "+":
        acc += n

total += acc
print(f"total (part 2): {total}")
