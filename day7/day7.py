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
        new_timelines = [0 for i in range(N_COLS)]

        for i, c in enumerate(row):
            if c == "S":
                new_hb[i] = True
                new_timelines[i] = 1
            elif has_beam[i]:
                if c == "^":
                    if i > 0:
                        new_hb[i-1] = True
                        new_timelines[i-1] += timelines[i]
                    if i < N_COLS-1:
                        new_hb[i+1] = True
                        new_timelines[i+1] += timelines[i]
                    n_splits += 1
                else:
                    new_hb[i] = True
                    new_timelines[i] += timelines[i]

        has_beam = new_hb
        timelines = new_timelines

print(f"(Part 1) Number of splits: {n_splits}")
print(f"(Part 2) Number of timelines: {sum(timelines)}")
