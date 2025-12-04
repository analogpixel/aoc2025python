file_name = "data/4_example.txt"
file_name = "data/4.txt"

puzzle = [ list(x.strip()) for x in open(file_name).readlines() ]

def get_xy(p, x, y):
    if y < 0 or y >= len(p) or x < 0 or x >= len(p[0]):
        return False
    return p[y][x]

def get_around(p, x,y):
    directions = [ [-1,-1], [0,-1], [1,-1], [-1,0], [1,0], [-1,1], [0,1], [1,1] ]
    return [ get_xy(p, x+d[0], y+d[1]) for d in directions ]

print(puzzle)

## part 1 
# total = 0
# for x in range(0, len(puzzle[0])):
#     for y in range(0, len(puzzle)):
#         if get_xy(puzzle, x,y) == "@":
#             _l = get_around(puzzle, x,y)
#             if _l.count('@') < 4:
#                 print(x,y,_l)
#                 total +=1
#


## Part 2
last = -99
loop_count = 0
all_total = 0
while True:
    total = 0
    removed = []
    for x in range(0, len(puzzle[0])):
        for y in range(0, len(puzzle)):
            if get_xy(puzzle, x,y) == "@":
                _l = get_around(puzzle, x,y)
                if _l.count('@') < 4:
                    #print(x,y,_l)
                    removed.append([x,y])
                    total +=1
                    all_total +=1 

    for r in removed:
        x,y = r
        puzzle[y][x] = '.'

    print("Total for this round:", total)

    if all_total == last:
        break
    else:
        last = all_total
        loop_count += 1

print(all_total, loop_count)
