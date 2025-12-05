file_name = "data/5_example.txt"
file_name = "data/5.txt"

_data = open(file_name).readlines()
_split = _data.index('\n')

ranges = []

for r in _data[0:_split]:
    bottom,top = [ int(x) for x in r.strip().split('-')]
    ranges.append( [bottom,top] )


## Part 1
total = 0
for check in [int(x.strip()) for x in _data[_split+1:]]:
    for r in ranges:
        bottom,top = r
        if check >= bottom and check <= top:
            total +=1
            break

print("Part 1:", total)


def merge_ranges(ranges):
    # Sort ranges by their start (bottom)
    ranges = sorted(ranges, key=lambda r: r[0])

    merged = []

    for r in ranges:
        if not merged:
            merged.append(r)
            continue

        last = merged[-1]

        # Check overlap or touching
        if r[0] <= last[1]:
            # Merge by extending the end
            last[1] = max(last[1], r[1])
        else:
            merged.append(r)

    return merged


new_ranges = merge_ranges(ranges)
total = 0
for r in new_ranges:
    total += r[1] - r[0] + 1

print("Part 2:", total)
