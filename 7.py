#!/usr/bin/env python

from functools import lru_cache

#puzzle_input = open("data/7_example.txt").readlines()
puzzle_input = open("data/7.txt").readlines()

beams = [ puzzle_input[0].index("S")  ]
split_count = 0

def part1(beams, puzzle_input):
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
    print("split count:", split_count)
    return split_count

@lru_cache(maxsize=None)
def part2(beam_idx, line_idx):
    if line_idx >= len(puzzle_input):
        print("eof")
        return 1

    # continue through file until you split
    while puzzle_input[line_idx][beam_idx] != "^":
        line_idx+=1
        if line_idx >= len(puzzle_input):
            return 1

    # if split then 
    return part2(beam_idx-1, line_idx+1 ) + part2(beam_idx+1, line_idx+1)

part1(beams, puzzle_input)
print( part2(beams[0],  1) )
