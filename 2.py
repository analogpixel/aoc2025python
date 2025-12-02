ranges = open("data/2_example.txt").readlines()[0].strip().split(',')
#ranges = open("data/2.txt").readlines()[0].strip().split(',')


total = 0
for r in ranges:
    top, bottom = [int(x) for x in r.split('-')]
    for i in range(top, bottom+1):
        s1 = str(i)
        s1_mid = len(s1) // 2
        if s1[0:s1_mid] == s1[s1_mid:]:
            total += i

print("Part1:", total)



def chunkstring(string, length):
    return list((string[0+i:length+i] for i in range(0, len(string), length)))


total = 0
for r in ranges:
    top, bottom = [int(x) for x in r.split('-')]
    found = False
    for i in range(top, bottom+1):
        s1 = str(i)
        s1_len = len(s1) 
        for j in range(1, s1_len):
            _l = chunkstring(s1, j)
            if len(set(_l)) == 1:
                total += i
                break

print("Part2:", total)



