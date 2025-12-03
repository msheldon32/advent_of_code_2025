# PART 1

acc = 0

def get_max_voltage(row):
    max_val = 0
    max_digit = float("-inf")

    for c in row[::-1]:
        d = int(c)
        max_val = max(max_val, d*10 + max_digit)
        max_digit = max(max_digit, d)

    return max_val

with open("input", "r") as f:
    for row in f:
        acc += get_max_voltage(row.strip())

print(f"total voltage: {acc}")

# PART 2
acc = 0

def get_max_voltage_2(row):
    maxs = [0 for i in range(12)]

    for c in row:
        d = int(c)
        new_maxs = [0 for i in range(12)]

        new_maxs[0] = max(d, maxs[0])
        
        for i in range(1,12):
            new_maxs[i] = max(maxs[i], (maxs[i-1]*10)+d)

        maxs = new_maxs

    return max(maxs)

with open("input", "r") as f:
    for row in f:
        acc += get_max_voltage_2(row.strip())

print(f"total voltage: {acc}")
