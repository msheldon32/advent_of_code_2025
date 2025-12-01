# PROBLEM 1

dial = 50
password = 0

with open("input", "r") as f:
    for row in f:
        abs_d = int(row[1:])
        if row[0] == "R":
            dial += abs_d
        else:
            dial -= abs_d
        dial += 100
        dial %= 100

        if dial == 0:
            password += 1

print(f"password (problem 1): {password}")


# PROBLEM 2
dial = 50
password = 0

with open("input", "r") as f:
    for row in f:
        abs_d = int(row[1:])

        if abs_d == 0:
            continue

        if row[0] == "R":
            dial += abs_d
        elif dial == 0:
            dial += 100
            dial -= abs_d
        else:
            dial -= abs_d

        while dial < 0:
            password += 1
            dial += 100

        if dial == 0:
            password += 1

        while dial >= 100:
            password += 1
            dial -= 100

print(f"password (problem 2): {password}")
