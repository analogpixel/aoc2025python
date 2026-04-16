#!/usr/bin/env python


puzzle_input = open("data/7_example.txt").readlines()
puzzle_input = open("data/7.txt").readlines()

beams = [ puzzle_input[0].index("S")  ]
split_count = 0

for line in puzzle_input[1:]:
    indices = [i for i, ch in enumerate(line) if ch == '^']    

    next_beam = []

    # beam hits splitter
    for b_split in set(indices) & set(beams):
        #print("beam split at:", b_split)
        next_beam.append( b_split -1)
        next_beam.append( b_split +1)
        split_count +=1

    # existing beams that don't intersect with splitter
    for n_split in set(beams) - set(indices):
        #print("beam NOT split at:", n_split)
        next_beam.append(n_split)

    beams = set(next_beam)

print(beams)
print("split count:", split_count)
