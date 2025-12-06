import re
from functools import reduce

file_name = "data/6_example.txt"
file_name = "data/6.txt"

def get_col(data, c):
    return [ x[c] for x in data ]

_data = open(file_name).readlines()

_numbers = _data[0:-1]
_operations = _data[-1].strip()

operations = re.split( r'\s+', _operations)
_numbers = [ re.split( r'\s+', x.strip() ) for x in _numbers]
numbers = [[int(n) for n in sublist] for sublist in _numbers]

total = 0
for col in range(len(numbers[0])):
    col_output = get_col(numbers, col)

    if operations[col] == '+':
        out = reduce(lambda x,y: x+y, col_output)
        total += out
    elif operations[col] == "*":
        out = reduce(lambda x,y: x*y, col_output)
        total += out
    else:
        print("ERROR")
    
print("Part 1 Total:", total)


## part 2
## read in the file 1 col at a time, and end when all rows report a space

_data = open(file_name).readlines()
_numbers = _data[0:-1]
opts     = _data[-1]

current_op = ""
col_num_list = []
total = 0
for i in range(0, len(_numbers[0]) ):
    found=False
    current_col = []
    for c in range(0, len(_numbers)):
        if i < len(opts) and opts[i] not in [' ', '\n']:
            current_op = opts[i]
        if _numbers[c][i] not in   [' ','\n']:
            current_col.append(_numbers[c][i])
            found=True

    if len(current_col) > 0:
        current_col_num = int("".join(current_col))
        col_num_list.append( current_col_num)
        #print(current_col_num, current_op)
    else:
        #print("space", col_num_list)
        if current_op == "+":
            out = reduce(lambda x,y: x+y, col_num_list)
        else:
            out = reduce(lambda x,y: x*y, col_num_list)
        
        total += out
        col_num_list = []
        #print("out:", out, total)

print("Part 2:", total)
