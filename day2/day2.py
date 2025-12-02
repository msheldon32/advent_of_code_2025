# PART 1
with open("input", "r") as f:
    ranges = f.read().split(",")
    ranges = [x.split("-") for x in ranges]
    ranges = [(int(x[0]), int(x[1])) for x in ranges]
ranges.sort()
print(ranges)
acc = 0

for fst, lst in ranges:
    for i in range(fst, lst+1):
        rep = str(i)
        if len(rep) % 2 == 1:
            continue
        mid = len(rep)//2
        if rep[:mid] == rep[mid:]:
            acc += i

print(f"total: {acc}")

# PART 2
def is_repeating(rep):
    n_digits = len(rep)

    for substr_len in range(1,(n_digits//2)+1):
        if n_digits % substr_len != 0:
            continue
        fst_substr = rep[:substr_len]
        it = substr_len
        is_repeating = True
        while it < len(rep):
            if rep[it:it+substr_len] != fst_substr:
                is_repeating = False
                break
            it += substr_len
        if is_repeating:
            return True
    return False

acc = 0


for fst, lst in ranges:
    for i in range(fst, lst+1):
        if is_repeating(str(i)):
            acc += i

print(f"total: {acc}")
