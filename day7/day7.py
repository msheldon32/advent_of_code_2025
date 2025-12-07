TEST = False
if TEST:
    INPUT_FILE = "input2"
    N_COLS = 15
else:
    INPUT_FILE = "input"
    N_COLS = 141

has_beam = [False for i in range(N_COLS)]
n_splits = 0

timelines = [0 for i in range(N_COLS)]

with open(INPUT_FILE, "r") as f:
    for row_no, row in enumerate(f):
        row = row.strip()
        new_hb = [False for i in range(N_COLS)]
        splits = set()
        for i, c in enumerate(row):
            if c == "S":
                new_hb[i] = True
                timelines[i] = 1
            elif has_beam[i]:
                if c == "^":
                    if i > 0:
                        new_hb[i-1] = True
                    if i < N_COLS-1:
                        new_hb[i+1] = True
                    n_splits += 1
                    splits.add(i)
                else:
                    new_hb[i] = True
        has_beam = new_hb

        new_timelines = [0 for i in range(N_COLS)]

        for i, x in enumerate(timelines):
            if i in splits:
                if i + 1 < N_COLS:
                    new_timelines[i+1] += x
                if i-1 >= 0:
                    new_timelines[i-1] += x
            else:
                new_timelines[i] += x
        timelines = new_timelines

print(f"(Part 1) Number of splits: {n_splits}")
print(f"(Part 2) Number of timelines: {sum(timelines)}")
