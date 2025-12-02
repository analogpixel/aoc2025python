d = open("data/1.txt").readlines()
#d = open("data/1_example.txt").readlines()

pos = int(d[0])
start_pos = pos
convert = {'L': -1, 'R': 1 }
moves = [ convert[x[0]] * int(x[1:]) for x in d[1:] ]


## Part 1
total = 0

for m in moves:
    pos = (pos + m) % 100
    print(pos)
    if pos == 0:
        total += 1

print("Part 1:", total)


## Part 2
total = 0
pos = start_pos

# 6599 correct answer
for m in moves:
    for i in range(0, abs(m)):
        if m < 0:
            pos -= 1
        else:
            pos += 1


        if pos == 100:
            pos = 0
        elif pos == -1:
            pos = 99

        if pos == 0:
            total +=1

print(total)
