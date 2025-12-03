data_file = "data/3_example.txt"
data_file = "data/3.txt"

joltage_lines = [ [int(j) for j in list(x.strip())] for x in open(data_file).readlines()]



def find_max2(j):
    _t = []
    for i in range(len(j)):
        _l = j[i+1:]
        if len(_l) > 0:
            _t.append( j[i]*10 + max(j[i+1:]) )
        else:
            _t.append(j[i])

    return max(_t)

def find_max_x(start_position, jolt_list ,num_size):
    jolt_size = len(jolt_list)
    i = start_position + 1 
    digits = []
    digits.append( jolt_list[start_position] )
    while True:
        current_digits = len(digits)
        needed_digits = num_size - current_digits
        search_end = jolt_size - needed_digits
        search_space = jolt_list[i:search_end+1]

        if len(search_space) <= 1:
            return int("".join([str(x) for x in list(digits + jolt_list[i:])]))
        else:
            big = max(search_space)
            big_idx = jolt_list.index(big, i)
            i = big_idx + 1
            digits.append(big)
            if len(digits) == num_size:
                return int("".join([str(x) for x in digits]))

def search_all(jolt_list, num_size):
    return max([ find_max_x(i, jolt_list, num_size) for i in range(0, len(jolt_list))])
    

total = 0
for j in joltage_lines:
    total += search_all(j, 12)
print("part 2:", total)

